#!/bin/bash

# Launch the UR5 robot
xterm&
echo "UR5 launched"
roslaunch ur_modern_driver ur5_bringup.launch robot_ip:=10.0.0.105

# Run the camera node
xterm&
echo "Camera node"
python /home/wisdom/catkin_ws/src/s2l/CameraNode_new.py

# Run the robot node
xterm&
echo "Robot node"
python /home/wisdom/catkin_ws/src/s2l/robot_node_opt.py

# Run the trajectory optimization node
xterm&
echo "Trajectory optimization node launched"
python /home/wisdom/catkin_ws/src/s2l/real_robot_exp.py
