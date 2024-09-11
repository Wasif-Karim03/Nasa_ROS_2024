import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class RoverControlNode(Node):
    def __init__(self):
        super().__init__('rover_control_node')
        self.publisher_ = self.create_publisher(Twist, '/cmd_vel', 10)
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.move_rover)
        self.velocity_msg = Twist()

    def move_rover(self):
        # Send velocity commands to move the rover forward
        self.velocity_msg.linear.x = 0.5  # Forward velocity
        self.velocity_msg.angular.z = 0.1  # Slight turn
        self.publisher_.publish(self.velocity_msg)

def main(args=None):
    rclpy.init(args=args)
    node = RoverControlNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
