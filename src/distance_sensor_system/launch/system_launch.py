import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    # Find the parameter file path
    config = os.path.join(
        get_package_share_directory('distance_sensor_system'),
        'config',
        'params.yaml'
    )

    return LaunchDescription([
        Node(
            package='distance_sensor_system',
            executable='sensor_node',
            name='sensor_node',
            parameters=[config]
        ),
        Node(
            package='distance_sensor_system',
            executable='processing_node',
            name='processing_node',
            parameters=[config]
        ),
        Node(
            package='distance_sensor_system',
            executable='service_node',
            name='service_node',
            parameters=[config]
        )
    ])