from irobot_create_msgs.msg import LightringLeds, AudioNote
from geometry_msgs.msg import Twist, PoseWithCovarianceStamped
from nav_msgs.msg import OccupancyGrid
from std_msgs.msg import String
from sensor_msgs.msg import LaserScan
from custom_interfaces.action import RobotGoal

from rclpy.action import ActionServer, GoalResponse
from rclpy.action.server import ServerGoalHandle

import rclpy
from rclpy.node import Node
from rclpy.qos import qos_profile_sensor_data

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

        # Subscribe to the robot position
        self.pos_subscriber = self.create_subscription(PoseWithCovarianceStamped, '/robotN/pose', self.callback_pos, 10)
        self.pos_subscriber

        # Subscribe to the occupancy grid
        self.map_subscriber = self.create_subscription(OccupancyGrid, '/robotN/map', self.callback_map, 10)
        self.map_subscriber

        # Subscirbe to LiDAR raw data
        self.scan_sub = self.create_subscription(LaserScan, '/robotN/scan', self.callback_scan, 10)
        self.scan_sub

        # Publisher for velocity
        self.velocity_pub = self.create_publisher(Twist, '/robotN/cmd_vel', 10)


    # Callback for position
    def callback_pos(self, msg):
        self.x = msg.pose.pose.position.x
        self.y = msg.pose.pose.position.y
        self.ang = msg.pose.pose.orientation.z

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

                # DO STUFF HERE

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
    rclpy.init(args=args)
    node = GoToGoalNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()