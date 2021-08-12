import numpy as np
import IPython
from std_msgs.msg import Float32MultiArray
from rospy.numpy_msg import numpy_msg
from rospy_tutorials.msg import Floats
import rospy
import time
import timeit
from config import *

def send_command(arm_action, base_action, gripper_action):
    time.sleep(2)
    print ('Sent action is', arm_action)
    robot_msg = Float32MultiArray(data=[base_action[0], base_action[1],
                                      base_action[2], arm_action[0],
                                      arm_action[1], arm_action[2],
                                      arm_action[3], arm_action[4],
                                      arm_action[5], gripper_action])
    #rospy.loginfo(robot_msg)
    robot_pub.publish(robot_msg)

def main():
    global robot_pub

    rospy.init_node("traj_opt_node", anonymous=True, disable_signals=True)
    robot_pub = rospy.Publisher('/full_robot_command', Float32MultiArray,
                                                               queue_size=10)

    while not rospy.is_shutdown():
        arm_action = ARM_HOME_QPOS.copy()
        base_action = np.array([0.01,0.,0.])
        gripper_action = 0
        send_command(arm_action, base_action, gripper_action)
        time.sleep (5)
        arm_action = ARM_TEST_QPOS.copy()
        base_action = np.array([-0.01,0.,0.])
        gripper_action = 1
        send_command(arm_action, base_action, gripper_action)
        time.sleep(5)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        rospy.signal_shutdown("KeyboardInterrupt")
        raise
