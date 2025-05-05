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
from custom_interfaces.msg import FieldData 

import rclpy
import numpy as np
import os
import matplotlib.pyplot as plt

import math
import time

# Any additional imports here

# Decide your node class name
class GoalPub(Node):
    def __init__(self):

        # Change to have your node name
        super().__init__('goal_pub')

        self.map_subscriber = self.create_subscription(OccupancyGrid, '/robot2/map', self.callback_map, 10)
        self.maze_pub = self.create_publisher(FieldData, 'maze_data', 10)
        self.pos_subscriber = self.create_subscription(PoseWithCovarianceStamped, '/robot2/pose', self.callback_pos, 10)

    def move_agent(self, target):
      if self.is_valid(target) and self.obstacle_space[target]>25:
        self.agent_pos = target
        self.obstacle_space[target] = 0 # free space

    

    def frontier_explore(self):
        while self.frontiers:
            target = self.frontiers[0]
            #print(f"Moving to frontier {target}")
            self.move_agent(target)
            #print(self.obstacle_space)


    def is_valid(self, pos):
        x,y = pos
        return 0 <= x < self.width and 0 <= y < self.height


    def callback_pos(self, msg):
        self.x = msg.pose.pose.position.x
        self.y = msg.pose.pose.position.y
        self.ang = euler_from_quaternion([msg.pose.pose.orientation.x, msg.pose.pose.orientation.y, msg.pose.pose.orientation.z, msg.pose.pose.orientation.w])[2]

    
    def callback_map(self,msg):
        data = FieldData()
        data.goal_x = 1, data.goal_y = 1
        data.field_data = msg
        self.maze_pub.publish(data)

        self.resolution = round(msg.info.resolution,3)
        self.origin_x = msg.info.origin.position.x
        self.origin_y = msg.info.origin.position.y
        self.origin_ang = msg.info.origin.orientation.z
        
        self.width = msg.info.width
        self.height = msg.info.height

        robot_x = round((self.x-self.origin_x)/self.resolution)
        robot_y = round((self.y-self.origin_y)/self.resolution)
        
        occupancy_grid = msg.data

        row = 0
        while row < self.height:
            col = 0
            while col < self.width:
                real_x,real_y = self.index_to_real(col,row)
                point = occupancy_grid[col + (row*self.width)]

                if point > 25:
                    self.obstacle_space.append([real_x, real_y])

                if point == -1:
                    self.frontiers.append([real_x, real_y])

                col += 1
            row += 1

        



def main(args=None):
    rclpy.init(args=args)

    # Change to be your node class name
    node = GoalPub()

    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()