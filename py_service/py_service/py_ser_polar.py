from math import *
import rclpy
from rclpy.node import Node
from turtlesim.srv import Spawn

class MinimalServer(Node):

    def __init__(self):
        super().__init__('py_ser_ploar_node')
        self.server_ = self.create_service(Spawn, 'polar_coordinate', self.send_response_message)

    def send_response_message(self, request_message, response_message):
        a = sqrt(pow(request_message.x,2)+pow(request_message.y,2))
        b = degrees(atan(request_message.y/request_message.x))
        response_message.name = request_message.name
        self.get_logger().info('Response - Polar Radial Coordinate : %f, Polar Angular Coordinate : %f' % (a, b))
        return response_message

def main(args=None):
    rclpy.init(args=args)
    minimal_server = MinimalServer()
    rclpy.spin(minimal_server)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
