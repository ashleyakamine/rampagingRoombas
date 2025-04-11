from irobot_create_msgs.msg import LightringLeds, AudioNote
from geometry_msgs.msg import Twist, PoseWithCovarianceStamped
from nav_msgs.msg import OccupancyGrid
from std_msgs.msg import String
from sensor_msgs.msg import LaserScan
from custom_interfaces.action import RobotGoal
import numpy as np
from rclpy.action import ActionServer, GoalResponse
from rclpy.action.server import ServerGoalHandle
import rclpy
from rclpy.node import Node
from rclpy.qos import qos_profile_sensor_data
from rclpy.executors import MultiThreadedExecutor, ExternalShutdownException
from rclpy.callback_groups import ReentrantCallbackGroup

from tf_transformations import euler_from_quaternion

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

    def greedy_path(self, goal_x, goal_y):
        print("Starting greedy path search...")
        path = []
        current = (self.x, self.y)
        total_cost = 0
        visited = set()

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1),
                      (-1, -1), (-1, 1), (1, -1), (1, 1)]

        while current != (goal_x, goal_y):
            path.append(current)
            visited.add(current)
            neighbors = []

            for dr, dc in directions:
                nr, nc = current[0] + dr, current[1] + dc
                if 0 <= nr < self.height and 0 <= nc < self.width:
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
        self.visualize_path(path)
        print(f"Path found! Total cost: {total_cost}")

        rclpy.shutdown()

    def map_callback(self, msg):
        print("Map callback triggered!")

        self.width = msg.info.width
        self.height = msg.info.height
        self.resolution = self.resolution
        self.origin = (self.origin_x, self.origin_y)

        print(f"Map dimensions: {self.width}x{self.height}")
        print(f"Map resolution: {self.resolution}")
        print(f"Map origin: {self.origin}")

        self.map_data = np.array(msg.data).reshape((self.height, self.width))

        x_min = self.origin[0]
        y_min = self.origin[1]

        goal_x, goal_y = self.goal_coords
        start_x, start_y = self.start_coords

        goal_col = int((goal_x - x_min) / self.resolution)
        goal_row = int((goal_y - y_min) / self.resolution)
        start_col = int((start_x - x_min) / self.resolution)
        start_row = int((start_y - y_min) / self.resolution)

        print(f"Start (x, y): ({start_x}, {start_y}) â†’ grid ({start_row}, {start_col})")
        print(f"Goal  (x, y): ({goal_x}, {goal_y}) â†’ grid ({goal_row}, {goal_col})")

        self.goal = (goal_row, goal_col)
        self.start = (start_row, start_col)

        self.generate_cost_map()
        self.greedy_path()

    def generate_cost_map(self):
        self.cost_map = np.zeros((self.height, self.width), dtype=int)
        for row in range(self.height):
            for col in range(self.width):
                val = self.map_data[row][col]
                if val >= 30: # is obstacle
                    self.cost_map[row][col] = 1000
                elif (row, col) == self.goal:
                    self.cost_map[row][col] = 0
                else:
                    dist = math.hypot(self.goal[0] - row, self.goal[1] - col)
                    self.cost_map[row][col] = int(round(dist))
        print("Cost map generated.")


    # Excecute callback
    def execute_callback(self, goal_handle):
        goal_x, goal_y = goal_handle.request.goal_x, goal_handle.request.goal_y
        result = RobotGoal.Result()

        # using cost map, calc path from curr_pos to goal

        # loop thru waypoints until goal

    # Callback for action goal
    def goal_callback(self, goal_request):
        self.get_logger().info("Recieved goal request")
        if (goal_request.goal_x, goal_request.goal_y) in self.obstacle_space:
            self.get_logger().warn("Goal is in an obstacle")
            return GoalResponse.REJECT
        else:
            self.get_logger().info("Accepted goal")
            return GoalResponse.ACCEPT

    # Callback for position
    def callback_pos(self, msg):
        self.x = msg.pose.pose.position.x
        self.y = msg.pose.pose.position.y
        self.ang = euler_from_quaternion([msg.pose.pose.orientation.x, msg.pose.pose.orientation.y, msg.pose.pose.orientation.z, msg.pose.pose.orientation.w])[2]

    # index in map to real x y
    def index_to_real(self,col,row):
        real_x = round((col*self.resolution) + self.origin_x,2)
        real_y = round((row*self.resoltuion) + self.origin_y,2)
        return real_x,real_y

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