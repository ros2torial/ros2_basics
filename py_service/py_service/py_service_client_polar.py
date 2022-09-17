import sys
import rclpy
from rclpy.node import Node
from turtlesim.srv import Spawn

class MinimalClientAsync(Node):

    def __init__(self):
        super().__init__('py_service_client_polar')
        self.client_ = self.create_client(Spawn, 'polar_coordinate')
        while not self.client_.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting again...')
        self.request_message = Spawn.Request()

    def send_request_message(self, x, y, theta):
        self.request_message.x = x
        self.request_message.y = y
        self.request_message.theta = theta
        self.get_logger().info('Sending - X Coordinate : %f, Y Coordinate : %f' % (self.request_message.x, self.request_message.y))
        self.future = self.client_.call_async(self.request_message)
        rclpy.spin_until_future_complete(self, self.future)
        return self.future.result()

def main(args=None):
    rclpy.init(args=args)
    minimal_client = MinimalClientAsync()
    response_message = minimal_client.send_request_message(float(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3]))
    minimal_client.get_logger().info('Success')
    minimal_client.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
