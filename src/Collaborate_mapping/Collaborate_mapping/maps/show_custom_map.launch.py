from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node

def generate_launch_description():
    # Declare launch arguments
    map_file_arg = DeclareLaunchArgument(
        'map_file',
        default_value='path/to/your/custom/map.yaml',
        description='Full path to the map file to load')

    rviz_config_file_arg = DeclareLaunchArgument(
        'rviz_config_file',
        default_value='/home/endeleze/Desktop/ros2/UNav_ws/src/Collaborate_mapping/Collaborate_mapping/maps/config.rviz',
        description='Full path to the RVIZ2 configuration file')

    # Load launch configuration values
    map_file = LaunchConfiguration('map_file')
    rviz_config_file = LaunchConfiguration('rviz_config_file')

    # Define map_server node
    map_server_node = Node(
        package='nav2_map_server',
        executable='map_server',
        name='map_server',
        output='screen',
        parameters=[{'yaml_filename': map_file}])

    # Define RVIZ2 node
    rviz_node = Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        output='screen',
        arguments=['-d', rviz_config_file])

    # Create and return launch description
    return LaunchDescription([
        map_file_arg,
        rviz_config_file_arg,
        map_server_node,
        rviz_node,
    ])
