import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Point
from sensor_msgs.msg import Image
from std_msgs.msg import Header

class ImageReplacer(Node):
    def __init__(self):
        super().__init__('image_replacer')
        self.publisher = self.create_publisher(Image, 'image_data', 10)
        self.subscription = self.create_subscription(Point, 'robot_position', self.robot_position_callback, 10)

        # Load initial image dataset and their 2D locations
        self.images = [
            # (2D_location, image_data)
            # ...
        ]
        self.boundary = (100, 100)  # Set environment boundaries (x, y)

    def robot_position_callback(self, msg: Point):
        # Check if the robot is within the boundaries
        if 0 <= msg.x < self.boundary[0] and 0 <= msg.y < self.boundary[1]:
            # Find the oldest image and replace it with the new one
            oldest_image = min(self.images, key=lambda img: img[0].header.stamp)
            oldest_image[0].header.stamp = self.get_clock().now().to_msg()
            oldest_image[1] = msg  # Update 2D location

            # Publish the new image
            self.publisher.publish(oldest_image[0])

def main(args=None):
    rclpy.init(args=args)

    image_replacer = ImageReplacer()
    rclpy.spin(image_replacer)

    # image_replacer.destroy_node()
    # rclpy.shutdown()

if __name__ == '__main__':
    main()
