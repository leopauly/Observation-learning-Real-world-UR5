import numpy as np
import IPython
from std_msgs.msg import Float32MultiArray
from rospy.numpy_msg import numpy_msg
from rospy_tutorials.msg import Floats
import rospy
import control_sequences
import time
import timeit
import config 

def send_command():
    time.sleep(2)
    arm_action =
    robot_msg = Float32MultiArray(data=[arm_action[0], arm_action[1],
                                      arm_action[2], arm_action[3],
                                      arm_action[4], arm_action[5]])
    rospy.loginfo(robot_msg)
    robot_pub.publish(robot_msg)

def main():
    global robot_pub

    rospy.init_node("traj_opt_node", anonymous=True, disable_signals=True)
    robot_pub = rospy.Publisher('/robot_command', Float32MultiArray,
                                                               queue_size=10)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        rospy.signal_shutdown("KeyboardInterrupt")
        raise
