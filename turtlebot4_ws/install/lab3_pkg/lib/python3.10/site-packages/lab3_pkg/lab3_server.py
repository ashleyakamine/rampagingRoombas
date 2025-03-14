from irobot_create_msgs.msg import LightringLeds, AudioNote
from geometry_msgs.msg import Twist
from std_msgs.msg import String
from sensor_msgs.msg import LaserScan, BatteryState
from irobot_create_msgs.msg import DockStatus

import rclpy
from rclpy.node import Node
from rclpy.qos import qos_profile_sensor_data
from custom_interfaces.srv import GetSummary

class BatteryServer(Node):
    def __init__(self):
        super().__init__('battery_server_node')
        self.velocity_cap = 0.4
        self.obstacle_detected = False
        self.obstacle_distance = 1


        self.scan_subscriber = self.create_subscription(LaserScan, '/robot2/scan', self.scan_callback, 10)
        self.vel_filtered_publish = self.create_publisher(Twist, 'robot2/cmd_vel', 10)
        self._vel_unfiltered = self.create_subscription(Twist, '/robot2/cmd_vel_unfiltered', self.call_unfiltered_callback, 10)
        self.led_publish = self.create_publisher(LightringLeds, '/robot2/cmd_lightring', qos_profile_sensor_data)

        self.battery_subscriber = self.create_subscription(BatteryState, '/robot2/battery_state', self.battery_callback, 10)
        self.dock_subscriber = self.create_subscription(DockStatus, '/robot2/dock_status', self.dock_callback, 10)

        self.summary_service = self.create_service(GetSummary, "get_state_summary", self.summary_service_callback)

    def summary_service_callback(self, request, response):
        get_summary = request.get_summary

        if(get_summary == 'yes'):
            response.summary = f"Rampaging Roomba Prime 2 \n {self.charge_level} \n {self.is_docked} \n {self.velocity_cap}"
        else: 
            response.summary = "No summary for you then"

        response.success = True
        return response

    def battery_callback(self, msg):
        self.charge_level = msg.percentage * 100.0

    def dock_callback(self, msg):
        self.is_docked = msg.is_docked

    def call_unfiltered_callback(self, msg):
        lightring_msg = LightringLeds()
        lightring_msg.header.stamp = self.get_clock().now().to_msg()
        lightring_msg.override_system = True
        # message_data = msg.data # THIS LINE WILL DEPEND ON DATA TYPE
        new_vel = Twist()

        if self.obstacle_detected:
            new_vel.linear.x = 0.0
            for i in range(6):
                lightring_msg.leds[i].red = 255
                lightring_msg.leds[i].blue = 255
                lightring_msg.leds[i].green = 0

        elif msg.linear.x > self.velocity_cap:
            new_vel.linear.x = self.velocity_cap
            for i in range(6):
                lightring_msg.leds[i].red = 255
                lightring_msg.leds[i].blue = 0
                lightring_msg.leds[i].green = 0

        else :
            new_vel.linear.x = msg.linear.x
            for i in range(6):
                lightring_msg.leds[i].red = 0
                lightring_msg.leds[i].blue = 0
                lightring_msg.leds[i].green = 255

        

        new_vel.angular.z = msg.angular.z

        self.get_logger().info(str(msg.linear.x) + " " + str(new_vel.linear.x))

        self.vel_filtered_publish.publish(new_vel)
        self.led_publish.publish(lightring_msg)
    
    def scan_callback(self, msg):
        self.obstacle_detected = False
        range_min = msg.range_min
        range_max = msg.range_max

        for i in msg.ranges[200:340]:
            if i >= range_min or i <= range_max:
                if i < self.obstacle_distance:
                    self.obstacle_detected = True
                


def main(args=None):
    rclpy.init(args=args)

    node = BatteryServer()

    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()