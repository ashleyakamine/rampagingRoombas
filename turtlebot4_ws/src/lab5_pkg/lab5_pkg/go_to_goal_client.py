import rclpy
from rclpy.node import Node

from rclpy.action import ActionClient
from rclpy.action.client import ClientGoalHandle, GoalStatus

from custom_interfaces.action import RobotGoal

class GoToGoalClient(Node):

    def __init__(self):

        super().__init__('go_to_goal_client')

        self.go_to_goal_client = ActionClient(self, RobotGoal, "robot_goal")

        while not self.go_to_goal_client.wait_for_server(1.0):
            self.get_logger().info("Waiting for server")


    # Send Goal
    def send_goal(self, goal_x, goal_y, goal_theta):
        goal = RobotGoal.Goal()
        goal.goal_x = goal_x
        goal.goal_y = goal_y
        goal.goal_theta = goal_theta
        self.go_to_goal_client.send_goal_async(goal, feedback_callback=self.goal_feedback_callback).add_done_callback(self.goal_response_callback)


    # Process Goal Accept/Reject
    def goal_response_callback(self, future):
        goal_handle = future.result()

        if goal_handle.accepted:
            self.get_logger().info("Goal got accepted")
            goal_handle.get_result_async().add_done_callback(self.goal_result_callback)
        else:
            self.get_logger().info("Goal got rejected: ripperoni")


    # Process Goal Feedback
    def goal_feedback_callback(self, feedback_msg):
        current_x = feedback_msg.feedback.current_x
        current_y = feedback_msg.feedback.current_y
        current_theta = feedback_msg.feedback.current_theta
        distance_from_goal = feedback_msg.feedback.distance_from_goal
        self.get_logger().info(f"current_x: {current_x} \n current_y: {current_y} \n current_theta: {current_theta} \n distance_from_goal: {distance_from_goal} \n")


    # Process Action Result
    def goal_result_callback(self, future):
        result = future.result().result
        status = future.result().status

        if status == GoalStatus.STATUS_SUCCEEDED:
            self.get_logger().info("Success!")
            success = result.success
            self.get_logger().info(success)
        else:
            self.get_logger().info("Failed in goal result callback")

        rclpy.shutdown()

def main(args=None):
    # Start up rclpy
    rclpy.init(args=args)

    # Create instance of node
    action_client = GoToGoalClient()

    # Send the goal
    action_client.send_goal(float(input("Enter x: ")), float(input("Enter y: ")), float(input("Enter theta: ")))

    # Normal spin, yay! (callback handles shutdown)
    rclpy.spin(action_client)

if __name__ == '__main__':
    main()