from irobot_create_msgs.msg import LightringLeds, AudioNote
from geometry_msgs.msg import Twist, PoseWithCovarianceStamped
from nav_msgs.msg import OccupancyGrid
from std_msgs.msg import String
from sensor_msgs.msg import LaserScan
from custom_interfaces.action import RobotGoal

from rclpy.action import ActionServer, GoalResponse
from rclpy.action.server import ServerGoalHandle
from rclpy.node import Node
from rclpy.qos import qos_profile_sensor_data
from rclpy.executors import MultiThreadedExecutor, ExternalShutdownException
from rclpy.callback_groups import ReentrantCallbackGroup

from tf_transformations import euler_from_quaternion

import rclpy
import numpy as np
import os
import matplotlib.pyplot as plt

import math

class GoToGoalNode(Node):
    def __init__(self):
        super().__init__('go_to_goal')
        
        # pi
        self.PI = 3.14159265358979323846
        
        # False until scan sees something
        self.obstacle = False

        # Set by pose from pose topic
        self.x = 0
        self.y = 0
        self.ang = 0
        self.goal_x = 0
        self.goal_y = 0

        # Robot radius
        self.robot_radius = 0.3

        # Meta data from occupancy grid
        self.resoltuion = 0.05 # Default 5cm
        self.width = 0
        self.height = 0
        self.origin_x = 0.0
        self.origin_y = 0.0
        self.origin_ang = 0.0

        # Empty lists to add obstacles to
        self.obstacle_space = []

        # Subscribe to the robot position
        self.pos_subscriber = self.create_subscription(PoseWithCovarianceStamped, '/robot2/pose', self.callback_pos, 10)
        self.pos_subscriber

        # Subscribe to the occupancy grid
        self.map_subscriber = self.create_subscription(OccupancyGrid, '/robot2/map', self.callback_map, 10)
        self.map_subscriber

        # Subscirbe to LiDAR raw data
        self.scan_sub = self.create_subscription(LaserScan, '/robot2/scan', self.callback_scan, 10)
        self.scan_sub

        # Publisher for velocity
        self.velocity_pub = self.create_publisher(Twist, '/robot2/cmd_vel', 10)

        # Action server
        self.goal_action_server = ActionServer(self, RobotGoal, "robot_goal", goal_callback=self.goal_callback, execute_callback=self.execute_callback)

    def go_to_waypoint(self, waypoint_x, waypoint_y):
        goal_x, goal_y = waypoint_x, waypoint_y

        curr_dist = math.sqrt(((goal_x - self.x) ** 2) + ((goal_y - self.y) ** 2))
        while curr_dist > 0.5:
            new_vel = Twist()

            ang_diff = abs(self.ang - math.atan2((goal_y - self.y), (goal_x - self.x)))
            curr_dist = math.sqrt(((goal_x - self.x) ** 2) + ((goal_y - self.y) ** 2))

            self.get_logger().info(f"\nself.ang: {self.ang} \ngoal_ang:{math.atan2((goal_y - self.y), (goal_x - self.x))}")
            
            if abs(ang_diff > 0.25):
                new_vel.linear.x = 0.0
                new_vel.angular.z = 0.25
            else:
                new_vel.angular.z = 0.0
                if self.obstacle:
                    self.get_logger().warn("Obstacle Detected. Aborting")
                    new_vel.linear.x = 0.0
                    new_vel.angular.x = 0.0
                else:
                    new_vel.linear.x = 0.5 if curr_dist > 1.5 else 0.5 * (curr_dist / 1.5)
        
            self.velocity_pub.publish(new_vel)  

    # index in map to real x y
    def index_to_real(self,col,row):
        real_x = round((col*self.resolution) + self.origin_x,2)
        real_y = round((row*self.resoltuion) + self.origin_y,2)
        return real_x,real_y

    def real_to_index(self, col, row):
        index_x = round((col - self.origin_x) / self.resolution)
        index_y = round((row - self.origin_y) / self.resolution)
        return index_x, index_y

    def greedy_path(self, goal_x, goal_y):
        print("Starting greedy path search...")
        path = []
        current = self.real_to_index(self.x, self.y)
        total_cost = 0
        visited = set()
        print(f'greedy_path: x: {self.x}, y: {self.y}')

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1),
                      (-1, -1), (-1, 1), (1, -1), (1, 1)]

        while current != (goal_x, goal_y):
            path.append(current)
            visited.add(current)
            neighbors = []

            for dr, dc in directions:
                nr, nc = current[0] + dr, current[1] + dc
                if 0 <= nr < self.width and 0 <= nc < self.height:
                    if (nr, nc) not in visited and self.cost_map[nr][nc] < 1000:
                        neighbors.append((self.cost_map[nr][nc], (nr, nc)))

            if not neighbors:
                print("No path found.")
                return

            neighbors.sort()
            next_node = neighbors[0][1]
            print(f"Moving to {next_node} with cost {self.cost_map[next_node[0]][next_node[1]]}")
            total_cost += self.cost_map[next_node[0]][next_node[1]]
            current = next_node

        path.append((goal_x, goal_y))
        # self.visualize_path(path)
        print(f"Path found! Total cost: {total_cost}")

        return path


    # Excecute callback
    def execute_callback(self, goal_handle):
        goal_x, goal_y = goal_handle.request.goal_x, goal_handle.request.goal_y
        result = RobotGoal.Result()

        # using cost map, calc path from curr_pos to goal
        path = self.greedy_path(goal_x, goal_y)
        for point in path:
            self.go_to_waypoint(point[0], point[1])

            curr_dist = math.sqrt(((goal_x - self.x) ** 2) + ((goal_y - self.y) ** 2))
            feedback = RobotGoal.Feedback()
            feedback.current_x = float(self.x)
            feedback.current_y = float(self.y)
            feedback.current_theta = float(self.ang)
            feedback.distance_from_goal = float(curr_dist)
            goal_handle.publish_feedback(feedback)

        goal_theta = goal_handle.request.goal_theta
        self.get_logger().info(f"-- At goal -- \nself.ang: {self.ang} \ngoal_theta:{goal_theta}")
        
        new_vel = Twist()

        while abs(self.ang - goal_theta) > 0.25:
            new_vel.linear.x = 0.0
            new_vel.angular.z = 0.25

            self.velocity_pub.publish(new_vel)

            self.get_logger().info(f"At goal, turning... self.ang: {self.ang}")

        new_vel.linear.x = 0.0
        new_vel.angular.z = 0.0

        self.velocity_pub.publish(new_vel)

        self.get_logger().info("Suceeded")
        goal_handle.succeed()
        result.success = True
        return result   
    


    # Callback for action goal
    def goal_callback(self, goal_request):
        self.get_logger().info("Recieved goal request")
        if (goal_request.goal_x, goal_request.goal_y) in self.obstacle_space:
            self.get_logger().warn("Goal is in an obstacle")
            return GoalResponse.REJECT
        else:
            self.get_logger().info("Accepted goal")
            self.goal_x = goal_request.goal_x
            self.goal_y = goal_request.goal_y
            return GoalResponse.ACCEPT

    # Callback for position
    def callback_pos(self, msg):
        self.x = msg.pose.pose.position.x
        self.y = msg.pose.pose.position.y
        self.ang = euler_from_quaternion([msg.pose.pose.orientation.x, msg.pose.pose.orientation.y, msg.pose.pose.orientation.z, msg.pose.pose.orientation.w])[2]


    def euclidian_distance(self, x_f, y_f, x_0, y_0):
        return ( (x_f - x_0)**2 + (y_f - y_0)**2  )**(1/2)

    # get occupancy grid and find free, unknown, obstacle space
    def callback_map(self,msg):
        self.resolution = round(msg.info.resolution,3)
        # The origin of the map [m, m, rad].  This is the real-world pose of the cell (0,0) in the map
        self.origin_x = msg.info.origin.position.x
        self.origin_y = msg.info.origin.position.y
        self.origin_ang = msg.info.origin.orientation.z
        
        # How many columns (width) and rows (height)
        self.width = msg.info.width
        self.height = msg.info.height

        # Where is robot in map frame in col,row indices (NOT METERS!!)
        robot_x = round((self.x-self.origin_x)/self.resolution)
        robot_y = round((self.y-self.origin_y)/self.resolution)
        
        # Occupancy grid data in one big list
        occupancy_grid = msg.data
        self.cost_map = np.zeros((self.width, self.height))

        # Empty lists to add obstacles to
        self.obstacle_space = []
        
        row = 0
        while row < self.height:
            col = 0
            while col < self.width:
                real_x,real_y = self.index_to_real(col,row)
                point = occupancy_grid[col + (row*self.width)]

                if point > 25:
                    self.obstacle_space.append([real_x, real_y])

                col += 1
            row += 1

        row = 0

        while row < self.height:
            col = 0
            while col < self.width:
                real_x,real_y = self.index_to_real(col,row)
                for obs in self.obstacle_space:
                    obs_x, obs_y = obs[0],obs[1]
                    if self.euclidian_distance(obs_x, obs_y, real_x, real_y) < 0.3:
                        self.cost_map[col][row] == 1000
                    else :
                        self.cost_map[col][row] = round(self.euclidian_distance(self.goal_x,self.goal_y,real_x,real_y))

                col += 1
            row += 1

        self.map_image()

    def map_image(self):
        map_array = np.array(self.cost_map, dtype=np.int16)

        image = np.ones((self.width, self.height, 3), dtype=np.uint8) * 255 

        for i in range(self.width):
            for j in range(self.height):
                val = map_array[i, j]
                if val == 1000:
                    image[i, j] = [0, 0, 0]
                elif val >= 0:
                    image[i, j] = [190, 190, 190]

        # output_path = os.path.join(os.path.expanduser('~/rampagingRoombas/ros2_ws/src/lab6_pkg'), 'cost_map.png')
        # plt.imsave('./', image)
        # self.get_logger().info(f"Map image with path saved to: {output_path}")



    def callback_scan(self, msg):
        # Check to make sure not any in front obstacles at any time
        ## NOTE: this is not our obstacle avoidance, this is still jsut stop if obstacle
        range_min = msg.range_min
        range_max = msg.range_max

        self.obstacle = False
        
        # front range is a:b (total range is 0:1080)
        a = 200
        b = 340

        for angle in range(a,b):
            scan_point = msg.ranges[angle]
            
            if (scan_point <= range_min) or (scan_point >= range_max):
                pass
            else:
                if scan_point <= 0.7:
                    # detect obstacle
                    self.obstacle = True


def main(args=None):
    try:
        rclpy.init(args=args)
        node = GoToGoalNode()
        # Use a MultiThreadedExecutor to enable processing goals concurrently
        executor = MultiThreadedExecutor()
        rclpy.spin(node, executor=executor)
    except (KeyboardInterrupt, ExternalShutdownException):
        pass
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()