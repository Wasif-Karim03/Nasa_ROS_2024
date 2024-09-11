from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import ExecuteProcess

def generate_launch_description():
    return LaunchDescription([
        # Launch Gazebo with the rover model
        ExecuteProcess(
            cmd=['gazebo', '--verbose', '-s', 'libgazebo_ros_factory.so'],
            output='screen'),

        # Start the control node
        Node(
            package='my_rover_package',
            executable='rover_control_node',
            name='rover_control',
            output='screen'
        )
    ])
