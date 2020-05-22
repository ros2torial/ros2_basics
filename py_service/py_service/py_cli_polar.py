import sys
import rclpy
from rclpy.node import Node
from turtlesim.srv import Spawn

class MinimalClientAsync(Node):

    def __init__(self):
        super().__init__('py_cli_ploar_node')
        self.client_ = self.create_client(Spawn, 'polar_coordinate')
        while not self.client_.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting again...')
        self.request_message = Spawn.Request()

    def send_request_message(self):
        self.request_message.x = float(sys.argv[1])
        self.request_message.y = float(sys.argv[2])
        self.request_message.theta = float(sys.argv[3])
        self.get_logger().info('Sending - X Coordinate : %f, Y Coordinate : %f' % (self.request_message.x, self.request_message.y))
        self.future = self.client_.call_async(self.request_message)

def main(args=None):
    rclpy.init(args=args)
    minimal_client = MinimalClientAsync()
    minimal_client.send_request_message()

    while rclpy.ok():
        rclpy.spin_once(minimal_client)
        if minimal_client.future.done():
            try:
                response_message = minimal_client.future.result()
            except Exception as e:
                minimal_client.get_logger().info('Service call failed %r' % (e,))
        else:
            minimal_client.get_logger().info('Success')
        break

    minimal_client.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
