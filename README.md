# NASA ROS 2024 - Rover Simulation Project

A ROS2-based robotic rover simulation project designed for NASA applications. This project provides a complete simulation environment for a rover robot using ROS2, Gazebo physics simulator, and URDF robot modeling.

## 📋 Overview

This project implements a simulated rover robot with autonomous control capabilities. The system consists of a rover model defined in URDF format, a ROS2 control node for movement commands, and Gazebo integration for physics-based simulation. The rover can be controlled through velocity commands and visualized in a 3D simulation environment.

## ✨ Features

- **ROS2 Integration**: Full ROS2 (Robot Operating System 2) implementation for robot control
- **Gazebo Simulation**: Physics-based 3D simulation environment using Gazebo
- **URDF Robot Model**: Complete robot description with chassis and wheel assemblies
- **Velocity Control**: Autonomous movement control via `/cmd_vel` topic
- **Launch System**: Automated launch configuration for Gazebo and control nodes

## 🏗️ Project Structure

```
Nasa_ROS_2024-main/
├── Control_Node.py              # ROS2 control node for rover movement
├── ROS2_Launch.py                # Launch file for Gazebo and control node
├── Rover URDF.xml                # Robot model definition (URDF format)
├── Gazebo_Integration.xml        # Gazebo plugin configuration
├── ROS Package Directory Structure  # Package structure reference
└── README.md                     # This file
```

### Recommended ROS2 Package Structure

For a complete ROS2 package, organize files as follows:

```
my_rover_package/
├── launch/
│   └── launch_rover.py          # Launch files
├── src/
│   └── rover_control_node.py    # Source code for control node
├── urdf/
│   └── rover_model.urdf         # URDF robot models
├── CMakeLists.txt               # Build configuration
└── package.xml                  # Package manifest
```

## 🔧 Prerequisites

Before running this project, ensure you have the following installed:

- **ROS2** (Humble, Foxy, or compatible distribution)
  - Installation guide: [ROS2 Installation](https://docs.ros.org/en/humble/Installation.html)
- **Gazebo** (Gazebo Classic or Gazebo Fortress)
  - Installation: `sudo apt-get install gazebo11` (or appropriate version)
- **Python 3.8+**
- **ROS2 Python packages**:
  ```bash
  sudo apt-get install ros-<distro>-rclpy ros-<distro>-geometry-msgs ros-<distro>-launch-ros
  ```

## 🚀 Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd Nasa_ROS_2024-main
   ```

2. **Source ROS2 environment**:
   ```bash
   source /opt/ros/<your-ros2-distro>/setup.bash
   ```

3. **Install dependencies**:
   ```bash
   # Install ROS2 packages
   sudo apt-get update
   sudo apt-get install ros-<distro>-gazebo-ros-pkgs
   ```

4. **Build the package** (if using a proper ROS2 workspace):
   ```bash
   colcon build
   source install/setup.bash
   ```

## 📖 Usage

### Running the Simulation

1. **Start the launch file**:
   ```bash
   ros2 launch <package-name> ROS2_Launch.py
   ```
   
   Or run the launch file directly:
   ```bash
   python3 ROS2_Launch.py
   ```

2. **Run the control node separately** (if needed):
   ```bash
   python3 Control_Node.py
   ```

### Controlling the Rover

The rover is controlled through the `/cmd_vel` topic, which accepts `geometry_msgs/Twist` messages:
- `linear.x`: Forward/backward velocity (m/s)
- `angular.z`: Rotational velocity (rad/s)

The default control node sends:
- Forward velocity: `0.5 m/s`
- Angular velocity: `0.1 rad/s` (slight turn)

### Manual Control via Topic

You can manually publish velocity commands:
```bash
ros2 topic pub /cmd_vel geometry_msgs/msg/Twist "{linear: {x: 0.5, y: 0.0, z: 0.0}, angular: {x: 0.0, y: 0.0, z: 0.1}}"
```

## 🔍 Component Details

### Control Node (`Control_Node.py`)

The `RoverControlNode` class:
- Publishes velocity commands to `/cmd_vel` topic at 2 Hz (0.5 second intervals)
- Implements autonomous forward movement with slight turning
- Uses ROS2's `rclpy` Python client library

**Key Features**:
- Timer-based control loop
- Configurable velocity parameters
- ROS2 node lifecycle management

### Launch File (`ROS2_Launch.py`)

The launch configuration:
- Starts Gazebo simulator with ROS factory plugin
- Launches the rover control node
- Configures output to screen for debugging

### URDF Model (`Rover URDF.xml`)

The robot model includes:
- **Chassis**: Main body (0.5m × 0.3m × 0.1m box)
  - Mass: 10.0 kg
  - Inertial properties defined
  - Visual and collision geometries
  
- **Wheels**: Cylindrical wheels (radius: 0.05m)
  - Mass: 2.0 kg per wheel
  - Continuous joints for rotation
  - Damping and friction parameters

**Note**: The current URDF defines one wheel (front left) as an example. Additional wheels should be added following the same pattern.

### Gazebo Integration (`Gazebo_Integration.xml`)

Configuration for Gazebo ROS control plugin:
- Robot namespace: `/rover`
- Control period: 0.01 seconds (100 Hz)
- Enables ROS control interface for the robot

## 🛠️ Customization

### Modifying Rover Behavior

Edit `Control_Node.py` to change movement patterns:
```python
self.velocity_msg.linear.x = 0.5   # Change forward speed
self.velocity_msg.angular.z = 0.1  # Change turning rate
```

### Adjusting Robot Parameters

Modify `Rover URDF.xml` to:
- Change dimensions (box size, wheel radius)
- Adjust mass and inertia values
- Add additional wheels or sensors
- Modify joint properties

### Launch Configuration

Customize `ROS2_Launch.py` to:
- Add additional nodes
- Configure Gazebo world files
- Set up sensor plugins
- Include additional launch files

## 🐛 Troubleshooting

### Common Issues

1. **Gazebo not starting**:
   - Ensure Gazebo is properly installed
   - Check that display is available (for GUI)
   - Verify ROS2-Gazebo bridge is installed

2. **Control node not publishing**:
   - Verify ROS2 environment is sourced
   - Check topic availability: `ros2 topic list`
   - Monitor topic: `ros2 topic echo /cmd_vel`

3. **URDF parsing errors**:
   - Validate URDF syntax
   - Ensure all links and joints are properly defined
   - Check for missing closing tags

## 📝 Future Enhancements

- [ ] Complete wheel definitions (all four wheels)
- [ ] Add sensors (LIDAR, cameras, IMU)
- [ ] Implement path planning algorithms
- [ ] Add obstacle avoidance
- [ ] Create custom Gazebo world environments
- [ ] Implement teleoperation interface
- [ ] Add logging and data recording
- [ ] Performance optimization and profiling

## 📄 License

This project is developed for NASA applications. Please refer to the project license for usage terms.

## 🤝 Contributing

Contributions are welcome! Please ensure:
- Code follows ROS2 best practices
- URDF models are properly validated
- Launch files are tested before submission
- Documentation is updated accordingly

## 📧 Contact

For questions or issues related to this project, please refer to the project maintainers or open an issue in the repository.

---

**Note**: This project is designed for educational and research purposes. Ensure proper testing and validation before deployment in real-world scenarios.
