import rclpy
from rclpy.node import Node
from custom_interfaces.srv import GetSummary

class SumClient (Node):
    def __init__(self):
        super().__init__('state_summary_client_node')
        self.cool_client = self.create_client(GetSummary, "get_state_summary")

        while not self.cool_client.wait_for_service(1.0):
            self.get_logger().warn("Waiting for service to start")

    def request_summary(self, get_summary):
        request = GetSummary.Request()
        request.get_summary = get_summary

        self.response = self.cool_client.call_async(request)


def main(args=None):
    rclpy.init(args=args)

    node = SumClient()

    user_input = input("Do you want a summary? (Yes/No)").lower()

    node.request_summary(user_input)

    rclpy.spin_once(node)

    if node.response.done():
        response = node.response.result()
        node.get_logger().info(response.summary)

    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()