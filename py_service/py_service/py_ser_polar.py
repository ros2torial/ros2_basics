from turtlesim.srv import Spawn
from math import *
import rclpy
from rclpy.node import Node

class MinimalService(Node):

    def __init__(self):
        super().__init__('py_ser_ploar_node')
        self.srv = self.create_service(Spawn, 'polar_coordinate', self.add_two_ints_callback)

    def add_two_ints_callback(self, request, response):
        a = sqrt(pow(request.x,2)+pow(request.y,2))
        b = degrees(atan(request.y/request.x))
        response.name = request.name
        self.get_logger().info('Response - Polar Radial Coordinate : %f, Polar Angular Coordinate : %f' % (a, b))
        return response

def main(args=None):
    rclpy.init(args=args)
    minimal_service = MinimalService()
    rclpy.spin(minimal_service)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
