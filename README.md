

# Distance Sensor System - CS 353 Lab 1
Description and Purpose
    -This repository contains a ROS 2 package designed to process simulated distance sensor data and trigger safety alerts using a custom service interface. It was developed using strict Test-Driven Development (TDD) principle to ensure 100% test coverage for node initialization.

The system consists of three distinct nodes:
*  **Sensor Node:** Simulates and publishes distance readings (in meters) to the `distance` topic.
*  **Processing Node:** Subscribes to the raw distance readings, converts them into centimeters, and publishes the processed data to the `distance_cm` topic.
*  **Service Node:** Hosts a custom service (`SetThreshold.srv`) to dynamically set a minimum safe distance. It subscribes to the sensor readings and logs a warning if the distance falls below the safety threshold.

### Repository Structure
*   `distance_sensor_system`: Contains the Python source code, tests, configuration parameters, and launch files.
*   `distance_sensor_interfaces`: Contains the custom `.srv` definitions used by the Service Node.
*   `docs`: Contains the Technical Report and Lab Reflection PDFs.

### How to Build
To compile the system, navigate to the root of your workspace and use the `colcon` build tool. Run the following commands:
```bash

cd ~/Lab1_Intro-to-AI-Robotics


colcon build --packages-select distance_sensor_interfaces distance_sensor_system
```

### How to Run
Instead of launching individual nodes manually, this system uses a single Python launch file (`system_launch.py`) that boots up all three nodes simultaneously and dynamically passes variables from the `params.yaml` configuration file. 

To launch the system, open a terminal and run:
```bash

source install/setup.bash


ros2 launch distance_sensor_system system_launch.py
```

### How to Run Tests
This project relies on Test-Driven Development (TDD) using the `pytest` framework. To verify the code quality and node initialization, you can run the test suite using `colcon test`.
```bash

colcon test --packages-select distance_sensor_system


colcon test-result --all
```



