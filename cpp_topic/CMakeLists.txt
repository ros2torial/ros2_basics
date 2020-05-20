cmake_minimum_required(VERSION 3.5)
project(cpp_topic)

# Default to C++14
if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 14)
endif()

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(geometry_msgs REQUIRED)

set(dependencies "geometry_msgs" "rclcpp")
add_executable(cpp_pub_spiral src/cpp_pub_spiral.cpp)
ament_target_dependencies(cpp_pub_spiral ${dependencies})

add_executable(cpp_sub_spiral src/cpp_sub_spiral.cpp)
ament_target_dependencies(cpp_sub_spiral ${dependencies})

install(TARGETS
  cpp_pub_spiral
  cpp_sub_spiral
  DESTINATION lib/${PROJECT_NAME})

ament_package()
