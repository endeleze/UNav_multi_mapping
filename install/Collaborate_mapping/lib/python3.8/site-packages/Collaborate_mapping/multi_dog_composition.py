# multi_dog_composition.py

import rclpy
from rclpy.executors import MultiThreadedExecutor

from Collaborate_mapping.Image_replacer import ImageReplacer
from Collaborate_mapping.RobotDog import RobotDog


def main(args=None):
    rclpy.init(args=args)

    # Create the server node
    server_node = ImageReplacer()

    # Create the robot dog nodes
    robot_dogs = [RobotDog(i) for i in range(1, 5)]  # 4 robot dogs with IDs from 1 to 4

    # Add nodes to the executor
    executor = MultiThreadedExecutor()
    executor.add_node(server_node)
    for dog in robot_dogs:
        executor.add_node(dog)

    # Run the nodes
    try:
        executor.spin()
    except KeyboardInterrupt:
        pass

    # Shutdown and destroy nodes
    # executor.shutdown()
    # server_node.destroy_node()
    # for dog in robot_dogs:
    #     dog.destroy_node()

    # rclpy.shutdown()

if __name__ == '__main__':
    main()
