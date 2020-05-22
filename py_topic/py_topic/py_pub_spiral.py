import sys
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class MinimalPublisher(Node):

    def __init__(self):
        super().__init__('py_pub_spiral_node')
        self.publisher_ = self.create_publisher(Twist, 'turtle1/cmd_vel', 1)
        timer_period = 0.5  # seconds
        self.i = 0.0
        self.timer_ = self.create_timer(timer_period, self.publish_message)

    def publish_message(self):
        message = Twist()
        message.linear.x = float(sys.argv[1])
        message.angular.z = float(sys.argv[2]) + self.i
        self.get_logger().info('Sending - Linear Velocity : %f, Angular Velocity : %f' % (message.linear.x, message.angular.z))
        self.publisher_.publish(message)
        self.i += float(sys.argv[3])

def main(args=None):
    rclpy.init(args=args)
    minimal_publisher = MinimalPublisher()
    rclpy.spin(minimal_publisher)
    minimal_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
