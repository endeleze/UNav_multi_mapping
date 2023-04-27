import rclpy
from rclpy.action import ActionServer
from example_interfaces.srv import AddTwoInts

from rclpy.node import Node

from action_tutorials_interfaces.action import Fibonacci
import time

class Map_Server(Node):

    def __init__(self):
        super().__init__('map_server')
        self._action_server = ActionServer(
            self,
            Fibonacci,
            'fibonacci',
            self.execute_callback)
        self.srv = self.create_service(AddTwoInts, 'send_', self.add_two_ints_callback)

    def execute_callback(self, goal_handle):
        self.get_logger().info('Executing goal...')

        feedback_msg = Fibonacci.Feedback()
        feedback_msg.partial_sequence = [0, 1]

        for i in range(1, goal_handle.request.order):
            feedback_msg.partial_sequence.append(
                feedback_msg.partial_sequence[i] + feedback_msg.partial_sequence[i-1])
            self.get_logger().info('Feedback: {0}'.format(feedback_msg.partial_sequence))
            goal_handle.publish_feedback(feedback_msg)
            time.sleep(1)

        goal_handle.succeed()

        result = Fibonacci.Result()
        result.sequence = feedback_msg.partial_sequence
        return result


def main(args=None):
    rclpy.init(args=args)

    map_server= Map_Server()

    rclpy.spin(map_server)


if __name__ == '__main__':
    main()