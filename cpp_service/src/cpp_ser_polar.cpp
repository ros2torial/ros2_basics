#include "rclcpp/rclcpp.hpp"
#include "turtlesim/srv/spawn.hpp"
#include <math.h>
#include <memory>

void copy(const turtlesim::srv::Spawn::Request::SharedPtr req, turtlesim::srv::Spawn::Response::SharedPtr res)
{
  float a = sqrt(pow((req->x),2) + pow((req->y),2));
  float b = atan((req->y)/(req->x))*180/M_PI;
  res->name = req->name;
  RCLCPP_INFO(rclcpp::get_logger("rclcpp"), "Response - Polar Radial Coordinate : '%f', Polar Angular Coordinate : '%f'", a, b);
}

int main(int argc, char **argv)
{
  rclcpp::init(argc, argv);
  auto node = rclcpp::Node::make_shared("cpp_ser_polar_node");
  auto service = node->create_service<turtlesim::srv::Spawn>("polar_coordinate", &copy);
  rclcpp::spin(node);
  rclcpp::shutdown();
}

