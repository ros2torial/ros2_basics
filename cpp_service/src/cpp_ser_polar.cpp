#include <memory>
#include <math.h>
#include "rclcpp/rclcpp.hpp"
#include "turtlesim/srv/spawn.hpp"

using std::placeholders::_1;
using std::placeholders::_2;

class MinimalServer : public rclcpp::Node
{
  public:
    MinimalServer()
    : Node("cpp_ser_ploar_node")
    {
      server_ = this->create_service<turtlesim::srv::Spawn>("polar_coordinate", std::bind(&MinimalServer::send_response_message, this, _1, _2));
    }

  private:
    void send_response_message(const turtlesim::srv::Spawn::Request::SharedPtr request_message, turtlesim::srv::Spawn::Response::SharedPtr response_message)
    {
        float a = sqrt(pow((request_message->x),2) + pow((request_message->y),2));
        float b = atan((request_message->y)/(request_message->x))*180/M_PI;
        response_message->name = request_message->name;
        RCLCPP_INFO(this->get_logger(), "Response - Polar Radial Coordinate : '%f', Polar Angular Coordinate : '%f'", a, b);
    }
    rclcpp::Service<turtlesim::srv::Spawn>::SharedPtr server_;
};

int main(int argc, char * argv[])
{
  rclcpp::init(argc, argv);
  rclcpp::spin(std::make_shared<MinimalServer>());
  rclcpp::shutdown();
  return 0;
}


