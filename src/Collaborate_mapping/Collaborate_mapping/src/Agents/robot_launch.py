from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
import os
import pathlib


def generate_launch_description():
# Declare launch arguments
    namespace_arg = DeclareLaunchArgument(
    'namespace',
    default_value='',
    description='Namespace for the robot'
    )

    map_yaml_file_arg = DeclareLaunchArgument(
        'map_yaml_file',
        default_value='',
        description='Path to the map YAML file'
    )

    # Get launch configurations
    namespace = LaunchConfiguration('namespace')
    map_yaml_file = LaunchConfiguration('map_yaml_file')

    # Robot description
    robot_description = os.path.join(
        pathlib.Path().cwd(),'src','Collaborate_mapping','Collaborate_mapping', 'urdf', 'LittleDog.urdf'
    )

    # Robot state publisher
    robot_state_publisher_node = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        name='robot_state_publisher',
        namespace=namespace,
        output='screen',
        parameters=[{'robot_description': robot_description}]
    )

    # AMCL localization
    amcl_node = Node(
        package='nav2_amcl',
        executable='amcl',
        name='amcl',
        namespace=namespace,
        output='screen',
        parameters=[{'use_sim_time': True, 'yaml_filename': map_yaml_file}]
    )

    # Navigation
    bt_navigator_node = Node(
        package='nav2_bt_navigator',
        executable='bt_navigator',
        name='bt_navigator',
        namespace=namespace,
        output='screen',
        parameters=[{'use_sim_time': True}]
    )

    # Robot controller
    controller_node = Node(
        package='nav2_controller',
        executable='controller_server',
        name='controller_server',
        namespace=namespace,
        output='screen',
        parameters=[{'use_sim_time': True}]
    )

    # Planner
    planner_node = Node(
        package='nav2_planner',
        executable='planner_server',
        name='planner_server',
        namespace=namespace,
        output='screen',
        parameters=[{'use_sim_time': True}]
    )

    # Lifecycle manager
    lifecycle_manager_node = Node(
        package='nav2_lifecycle_manager',
        executable='lifecycle_manager',
        name='lifecycle_manager',
        namespace=namespace,
        output='screen',
        parameters=[{'use_sim_time': True}]
    )

    return LaunchDescription([
        namespace_arg,
        map_yaml_file_arg,
        robot_state_publisher_node,
        amcl_node,
        bt_navigator_node,
        controller_node,
        planner_node,
        lifecycle_manager_node
    ])
