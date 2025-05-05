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

class PotentialField(Node):
    def __init__(self):

        super().__init__('potential_field')

        self.resolution = 0.05 # Default 5cm
        self.width = 0
        self.height = 0
        self.origin_x = 0.0
        self.origin_y = 0.0
        self.origin_ang = 0.0

        self.obstacle_space = []
        
        self.pos_subscriber = self.create_subscription(PoseWithCovarianceStamped, '/robot2/pose', self.callback_pos, 10)
        self.goal_sub = self.create_subscription(FieldData, 'maze_data', self.callback_goal, 10)
        self.velocity_publish = self.create_publisher(String, '/robot2/cmd_vel', 10)

    
    ## HELPER METHODS ##

    def index_to_real(self,col,row):
        real_x = round((col*self.resolution) + self.origin_x,2)
        real_y = round((row*self.resolution) + self.origin_y,2)
        return real_x,real_y

    def real_to_index(self, col, row):
        index_x = round((col - self.origin_x) / self.resolution)
        index_y = round((row - self.origin_y) / self.resolution)
        return index_x, index_y

    def attractive_force(self, robot_pos):
        """Compute the attractive force towards the goal"""

        magnitude = 0.5 * self.k_att * euclidean_distance(robot_pos, self.goal)
        ang = math.atan2(self.goal[1] - robot_pos[1], self.goal[0] - robot_pos[0])
        return magnitude, ang

    def repulsive_force(self, robot_pos, obstacle_pos):
        """ Compute the repulsive force due to an obstacle """

        dist = euclidean_distance(robot_pos, obstacle_pos)
        if dist > self.d_threshold:
            return 0.0, 0.0
        magnitude = 0.5 * self.k_rep * ((1/dist)-(1/self.d_threshold)) ** 2
        ang = math.atan2(obstacle_pos[1] - robot_pos[1], obstacle_pos[0] - robot_pos[0])
        ang += math.pi
        return magnitude, ang

    ## CALLBACKS ##

    def callback_pos(self, msg):
        self.x = msg.pose.pose.position.x
        self.y = msg.pose.pose.position.y
        self.ang = euler_from_quaternion([msg.pose.pose.orientation.x, msg.pose.pose.orientation.y, msg.pose.pose.orientation.z, msg.pose.pose.orientation.w])[2]

    def callback_goal(self, msg):
        self.goal_x  = msg.goal_x
        self.goal_y  = msg.goal_y


def to_cartesian(vector):
    """Returns the cartesian version of the input polar vector"""
    vx = vector[0] * math.cos(vector[1])
    vy = vector[0] * math.sin(vector[1])
    return vx, vy


def to_polar(vector):
    """Returns the polar version of the input cartesian vector"""
    magnitude = math.sqrt(vector[0] ** 2 + vector[1] ** 2)
    ang = math.atan2(vector[1], vector[0])
    return magnitude, ang


def add_vectors(v1, v2):
    """returns the sum of two polar vectors"""
    v1_parts = to_cartesian(v1)
    v2_parts = to_cartesian(v2)
    result = v1_parts[0] + v2_parts[0], v1_parts[1] + v2_parts[1]
    return to_polar(result)


def euclidean_distance(p1, p2):
    """Compute the Euclidean distance between two points"""
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def main(args=None):
    rclpy.init(args=args)

    node = PotentialField()

    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()