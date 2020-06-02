# ros2_basics

</br>

## About

This Repository contains some basic ROS2 examples.

</br>

### Topic

#### C++

* To run `cpp_pub_spiral` executable

```bash
ros2 run cpp_topic cpp_pub_spiral
```

* To run `cpp_sub_spiral` executable

```bash
ros2 run cpp_topic cpp_sub_spiral
```

#### Python

* To run `py_pub_spiral` executable

```bash
ros2 run py_topic py_pub_spiral 2.0 2.0 0.2
ros2 run py_topic py_pub_spiral 1.0 3.0 -0.2
```

* To run `py_sub_spiral` executable

```bash
ros2 run py_topic py_sub_spiral
```

</br>

### Service

#### C++

* To run `cpp_ser_polar` executable

```bash
ros2 run cpp_service cpp_ser_polar
```

* To run `cpp_cli_polar` executable

```bash
ros2 run cpp_service cpp_cli_polar
```

#### Python

* To run `py_ser_polar` executable

```bash
ros2 run py_service py_ser_polar
```

* To run `py_cli_polar` executable

```bash
ros2 run py_service py_cli_polar 4.0 3.0 1.0
```
