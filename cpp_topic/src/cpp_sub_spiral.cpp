#include <memory>
#include "rclcpp/rclcpp.hpp"
#include "geometry_msgs/msg/twist.hpp"

using std::placeholders::_1;

class MinimalSubscriber : public rclcpp::Node
{
  public:
    MinimalSubscriber()
    : Node("cpp_sub_spiral_node")
    {
      subscriber_ = this->create_subscription<geometry_msgs::msg::Twist>("turtle1/cmd_vel", 1, std::bind(&MinimalSubscriber::subscribe_message, this, _1));
    }

  private:
    void subscribe_message(const geometry_msgs::msg::Twist::SharedPtr message) const
    {
      RCLCPP_INFO(this->get_logger(), "Recieved - Linear Velocity : '%f', Angular Velocity : '%f'", message->linear.x, message->angular.z);
    }
    rclcpp::Subscription<geometry_msgs::msg::Twist>::SharedPtr subscriber_;
};

int main(int argc, char * argv[])
{
  rclcpp::init(argc, argv);
  rclcpp::spin(std::make_shared<MinimalSubscriber>());
  rclcpp::shutdown();
  return 0;
}
