# ros2_basics

</br>

## About

This Repository contains some basic ROS2 examples.

</br>

### Topic

#### C++

* To run `cpp_topic_publisher_spiral` executable

```bash
ros2 run cpp_topic cpp_topic_publisher_spiral
```

* To run `cpp_topic_subscriber_spiral` executable

```bash
ros2 run cpp_topic cpp_topic_subscriber_spiral
```

#### Python

* To run `py_topic_publisher_spiral` executable

```bash
ros2 run py_topic py_topic_publisher_spiral 2.0 2.0 0.2
ros2 run py_topic py_topic_publisher_spiral 1.0 3.0 -0.2
```

* To run `py_topic_subscriber_spiral` executable

```bash
ros2 run py_topic py_topic_subscriber_spiral
```

</br>

### Service

#### C++

* To run `cpp_service_server_polar` executable

```bash
ros2 run cpp_service cpp_service_server_polar
```

* To run `cpp_service_client_polar` executable

```bash
ros2 run cpp_service cpp_service_client_polar 4.0 3.0 1.0
```

#### Python

* To run `py_service_server_polar` executable

```bash
ros2 run py_service py_service_server_polar
```

* To run `py_service_client_polar` executable

```bash
ros2 run py_service py_service_client_polar 4.0 3.0 1.0
```
