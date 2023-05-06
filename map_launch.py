from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='nav2_map_server',
            executable='map_server',
            parameters=[
                {'yaml_filename': '/home/endeleze/Desktop/ros2/UNav_ws/src/Collaborate_mapping/Collaborate_mapping/maps/map.yaml'}
            ],
            output='screen'
        )
    ])
