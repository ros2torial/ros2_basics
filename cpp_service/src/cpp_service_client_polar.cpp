#include "rclcpp/rclcpp.hpp"
#include "turtlesim/srv/spawn.hpp"
#include <string>
#include <chrono>
#include <cstdlib>
#include <memory>

using namespace std::chrono_literals;

int main(int argc, char **argv)
{
  rclcpp::init(argc, argv);
  if(argc != 4){
    RCLCPP_INFO(rclcpp::get_logger("rclcpp"), "incorrect argument");
    return 1;
  }
  auto node = rclcpp::Node::make_shared("cpp_service_client_polar");
  auto client = node->create_client<turtlesim::srv::Spawn>("polar_coordinate");
  auto request = std::make_shared<turtlesim::srv::Spawn::Request>();
  request->x = std::stof(argv[1]);
  request->y = std::stof(argv[2]);
  request->theta = std::stof(argv[3]);

  while (!client->wait_for_service(1s)) {
    if (!rclcpp::ok()) {
      RCLCPP_ERROR(rclcpp::get_logger("rclcpp"), "Interrupted while waiting for the service. Exiting.");
      return 0;
    }
    RCLCPP_INFO(rclcpp::get_logger("rclcpp"), "service not available, waiting again...");
  }

  RCLCPP_INFO(rclcpp::get_logger("rclcpp"), "Sending - X Coordinate : '%f', Y Coordinate : '%f'", request->x, request->y);
  auto result = client->async_send_request(request);
  // Wait for the result.
  if (rclcpp::spin_until_future_complete(node, result) ==
    rclcpp::FutureReturnCode::SUCCESS)
  {
    RCLCPP_INFO(rclcpp::get_logger("rclcpp"), "Success");
  } else {
    RCLCPP_ERROR(rclcpp::get_logger("rclcpp"), "Failed to call service");
  }

  rclcpp::shutdown();
  return 0;
}
