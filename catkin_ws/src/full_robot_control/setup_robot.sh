# Setup robot

setup_bashrc() {

xterm -e "sudo cp ~/catkin_ws/src/full_robot_control/.bashrc ~/"}

 
setup_arm(){
 xterm -e "roslaunch ur_modern_driver ur5_bringup.launch robot_ip:=10.0.0.105"&

}

setup_gripper(){
xterm -e "rosrun robotiq_c_model_control CModelRtuNode.py /dev/ttyUSB0"&
xterm -e "rosrun robotiq_c_model_control CModelSimpleController.py"&
}

run_full_robot_node(){

xterm -e "python ~/catkin_ws/src/full_robot_control/full_robot_node.py"

}

setup_arm 
setup_gripper 
run_full_robot_node 
