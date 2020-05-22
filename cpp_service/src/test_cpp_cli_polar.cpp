#include <chrono>
#include <cstdlib>
#include <memory>
#include "rclcpp/rclcpp.hpp"
#include "turtlesim/srv/spawn.hpp"

using namespace std::chrono_literals;

class MinimalClientAsync : public rclcpp::Node
{
  public:
    MinimalClientAsync()
    : Node("cpp_cli_ploar_node")
    {
      client_ = this->create_client<turtlesim::srv::Spawn>("polar_coordinate");
    }

  private:
    void send_request_message()
    {
      auto request_message = std::make_shared<turtlesim::srv::Spawn::Request>();
      request_message->x = 5.0;
      request_message->y = 5.0;
      request_message->theta = 0.0; 
      RCLCPP_INFO(this->get_logger(), "Sending - X Coordinate : '%f', Y Coordinate : '%f'", request_message->x, request_message->y);
      auto response_message = client_->async_send_request(request_message);

  /*    if (rclcpp::spin_until_future_complete(Node, response_message) == rclcpp::executor::FutureReturnCode::SUCCESS)
      {
        RCLCPP_INFO(this->get_logger(), "Success");
      } 
      else 
      {
        RCLCPP_ERROR(this->get_logger(), "Failed to call service");
      }  */

    }
    rclcpp::Client<turtlesim::srv::Spawn>::SharedPtr client_;
};

int main(int argc, char * argv[])
{
  rclcpp::init(argc, argv);
  auto minimal_client = MinimalClientAsync();

  while (!minimal_client.client_->wait_for_service(1s)) 
  {
     if (!rclcpp::ok()) 
     {
        RCLCPP_ERROR(rclcpp::get_logger("rclcpp"), "Interrupted while waiting for the service. Exiting.");
        return 0;
     }
     RCLCPP_INFO(rclcpp::get_logger("rclcpp"), "service not available, waiting again...");
  }
  
  minimal_client.send_request_message();

  rclcpp::shutdown();
  return 0;
}


