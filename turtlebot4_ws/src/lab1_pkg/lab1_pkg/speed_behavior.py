from irobot_create_msgs.msg import LightringLeds, AudioNote
from geometry_msgs.msg import Twist
from std_msgs.msg import String

import rclpy
from rclpy.node import Node
from rclpy.qos import qos_profile_sensor_data

class SpeedBehaviorNode(Node):
    def __init__(self):
        super().__init__('speed_behavior_node')
        # Subscribe to the velocity commands
        self.vel_subscriber = self.create_subscription(Twist, '/robot2/cmd_vel', self.callback_vel, 10)
        self.vel_subscriber

        # Publisher for LEDs
        self.led_publish = self.create_publisher(LightringLeds, '/robot2/cmd_lightring', qos_profile_sensor_data)

        # Subscirbe to ip for testing
        self.ip_sub = self.create_subscription(String, '/robot2/ip', self.callback_ip, 10)
        self.ip_sub

        # Test publisher
        self.test_publish = self.create_publisher(String, 'test', 10)

    # Callback for velocity sub
    def callback_vel(self, msg):
        robot_vel_fwd = msg.linear.x
        self.get_logger().info(str(robot_vel_fwd))

        # Publish LED stuff in vel sub
        light_msg = self.set_lightring_colors(robot_vel_fwd)
        self.led_publish.publish(light_msg)
    

    # Set led colors based on velocity
    def set_lightring_colors(self,vel):
        lightring_msg = LightringLeds()
        lightring_msg.header.stamp = self.get_clock().now().to_msg()
        lightring_msg.override_system = True

        if vel < 0.1:
            for i in range(6):
                lightring_msg.leds[i].red = 0
                lightring_msg.leds[i].blue = 255
                lightring_msg.leds[i].green = 255

        elif vel < 0.3:
            for i in range(6):
                lightring_msg.leds[i].red = 255
                lightring_msg.leds[i].blue = 0
                lightring_msg.leds[i].green = 255

        else:
            for i in range(6):
                lightring_msg.leds[i].red = 255
                lightring_msg.leds[i].blue = 255
                lightring_msg.leds[i].green = 0

        return lightring_msg

    # Callback for ip
    def callback_ip(self, msg):
        self.get_logger().info('IP is "%s"' % msg.data)
        msg_test = String()

        # Testing publishing inside a sub callback
        # Seems to work?
        msg_test.data = 'Hi I see IP "%s"' % msg.data
        self.test_publish.publish(msg_test)
        
        

def main(args=None):
    rclpy.init(args=args)
    node = SpeedBehaviorNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()