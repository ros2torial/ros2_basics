cmake_minimum_required(VERSION 3.5)
project(cpp_topic)

# Default to C++17
if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 17)
endif()

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(geometry_msgs REQUIRED)

set(dependencies "geometry_msgs" "rclcpp")
add_executable(cpp_topic_publisher_spiral src/cpp_topic_publisher_spiral.cpp)
ament_target_dependencies(cpp_topic_publisher_spiral ${dependencies})

add_executable(cpp_topic_subscriber_spiral src/cpp_topic_subscriber_spiral.cpp)
ament_target_dependencies(cpp_topic_subscriber_spiral ${dependencies})

install(TARGETS
  cpp_topic_publisher_spiral
  cpp_topic_subscriber_spiral
  DESTINATION lib/${PROJECT_NAME})

ament_package()

