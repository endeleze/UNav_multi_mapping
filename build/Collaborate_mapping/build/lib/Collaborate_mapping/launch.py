from launch import LaunchDescription
from launch import LaunchService
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument, ExecuteProcess
from launch.substitutions import LaunchConfiguration
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
import os
import pathlib
import sys

def generate_launch_description():
    pkg_share = os.path.join(pathlib.Path().cwd(),'src','Collaborate_mapping','Collaborate_mapping')
    map_dir = os.path.join(pkg_share, 'maps')

    map_yaml_file = LaunchConfiguration('Map', default=os.path.join(map_dir, 'map.yaml'))

    declare_map_yaml_cmd = DeclareLaunchArgument(
        'Map',
        default_value=map_yaml_file,
        description='Path to the map YAML file')

    start_map_server_cmd = Node(
        package='nav2_map_server',
        executable='map_server',
        name='map_server',
        parameters=[{'yaml_filename': map_yaml_file}],
        output='screen')

    robots = []
    num_robots = 10

    for i in range(num_robots):
        robot_name = f'robot_{i}'
        robot_namespace = f'/robot_{i}'

        robots.append(
            IncludeLaunchDescription(
                PythonLaunchDescriptionSource(
                    os.path.join(pkg_share, 'src','Agents', 'robot_launch.py')
                ),
                launch_arguments={
                    'namespace': robot_namespace,
                    'map_yaml_file': map_yaml_file
                }.items()
            )
        )

    rviz_config_file = os.path.join(pkg_share, 'my_rviz_config.rviz')

    start_rviz_cmd = ExecuteProcess(
        cmd=['rviz2', '-d', rviz_config_file],
        output='screen'
    )

    return LaunchDescription([
        declare_map_yaml_cmd,
        start_map_server_cmd,
        *robots,
        start_rviz_cmd
    ])

def main(argv=None):
    ld = generate_launch_description()
    print("Launching:")
    print(ld)
    ls = LaunchService()
    ls.include_launch_description(ld)
    return ls.run()

if __name__ == '__main__':
    sys.exit(main())