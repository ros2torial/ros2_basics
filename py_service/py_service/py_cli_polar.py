import sys
from turtlesim.srv import Spawn
import rclpy
from rclpy.node import Node

class MinimalClientAsync(Node):

    def __init__(self):
        super().__init__('py_cli_ploar_node')
        self.cli = self.create_client(Spawn, 'polar_coordinate')
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting again...')
        self.req = Spawn.Request()

    def send_request(self):
        self.req.x = float(sys.argv[1])
        self.req.y = float(sys.argv[2])
        self.req.theta = float(sys.argv[3])
        self.get_logger().info('Sending - X Coordinate : %f, Y Coordinate : %f' % (self.req.x, self.req.y))
        self.future = self.cli.call_async(self.req)

def main(args=None):
    rclpy.init(args=args)
    minimal_client = MinimalClientAsync()
    minimal_client.send_request()

    while rclpy.ok():
        rclpy.spin_once(minimal_client)
        if minimal_client.future.done():
            try:
                response = minimal_client.future.result()
            except Exception as e:
                minimal_client.get_logger().info('Service call failed %r' % (e,))
        else:
            minimal_client.get_logger().info('Success')
        break

    minimal_client.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
