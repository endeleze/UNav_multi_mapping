import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Point
from sensor_msgs.msg import Image

class Collector(Node):
    def __init__(self):
        super().__init__('robot_dog')
        self.declare_parameter('robot_id', 1)
        robot_id = self.get_parameter('robot_id').value

        self.publisher = self.create_publisher(Point, 'robot_position', 10)
        self.subscription = self.create_subscription(Image, 'image_data', self.image_data_callback, 10)

        self.robot_id = robot_id

    def image_data_callback(self, msg: Image):
        self.get_logger().info('Robot dog {} received new image data'.format(self.robot_id))

        # Process the image data, e.g., store it, analyze it, etc.

    def publish_position(self, x, y):
        msg = Point()
        msg.x = x
        msg.y = y
        self.publisher.publish(msg)

def main(args=None):
    rclpy.init(args=args)

    robot_dog = Collector()

    rclpy.spin(robot_dog)

    # robot_dog.destroy_node()
    # rclpy.shutdown()

if __name__ == '__main__':
    main()
