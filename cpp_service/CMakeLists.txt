cmake_minimum_required(VERSION 3.5)
project(cpp_service)

# Default to C++17
if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 17)
endif()

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(turtlesim REQUIRED)

set(dependencies "turtlesim" "rclcpp")
add_executable(cpp_service_server_polar src/cpp_service_server_polar.cpp)
ament_target_dependencies(cpp_service_server_polar ${dependencies})

add_executable(cpp_service_client_polar src/cpp_service_client_polar.cpp)
ament_target_dependencies(cpp_service_client_polar ${dependencies})

install(TARGETS
  cpp_service_server_polar
  cpp_service_client_polar
  DESTINATION lib/${PROJECT_NAME})

ament_package()
