import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class MinimalSubscriber(Node):

    def __init__(self):
        super().__init__('py_sub_spiral_node')
        self.subscriber_ = self.create_subscription(Twist, 'turtle1/cmd_vel', self.subscribe_message, 1)
        self.subscriber_  # prevent unused variable warning

    def subscribe_message(self, msg):
        self.get_logger().info('Recieved - Linear Velocity : %f, Angular Velocity : %f' % (msg.linear.x, msg.angular.z))

def main(args=None):
    rclpy.init(args=args)
    minimal_subscriber = MinimalSubscriber()
    rclpy.spin(minimal_subscriber)
    minimal_subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
