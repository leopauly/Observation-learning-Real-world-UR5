#!/usr/bin/env python
import time
import roslib; roslib.load_manifest('ur_modern_driver')
import rospy
import actionlib
from control_msgs.msg import *
from trajectory_msgs.msg import *
from rospy.numpy_msg import numpy_msg
from rospy_tutorials.msg import Floats
from sensor_msgs.msg import JointState
import numpy as np
from std_msgs.msg import Float32MultiArray
JOINT_NAMES = ['shoulder_pan_joint', 'shoulder_lift_joint', 'elbow_joint',
               'wrist_1_joint', 'wrist_2_joint', 'wrist_3_joint']

client = None
TIMEOUT=2000


def full_robot_command_callback(data):
    global command
    command = data.data

def arm_state_callback(data):
    global robot_state

    if data.name == JOINT_NAMES:
        print ('Yes, this is the arm joint state')
        robot_state = np.array(data.position)
        print (robot_state)

def control_arm(current_state, desired_state):
    g = FollowJointTrajectoryGoal()
    g.trajectory = JointTrajectory()
    g.trajectory.joint_names = JOINT_NAMES
    g.trajectory.points = [
        JointTrajectoryPoint(positions=current_state, velocities=[0]*6, time_from_start=rospy.Duration(0)),
        JointTrajectoryPoint(positions=desired_state, velocities=[0]*6, time_from_start=rospy.Duration(DURATION))]
    client.send_goal(g)
    try:
        client.wait_for_result()
    except KeyboardInterrupt:
        client.cancel_goal()
        raise

def control_base():
    pass

def control_gripper():
    pass

def main():
    global arm_state # The robot's current state
    global TIMEOUT  # Max time to wait for message
    global DURATION # Control duration
    global command  # Full robot command
    global client    # Follow joint trajectory client for the arm

    # Initialize the robot node
    rospy.init_node("full_robot_node", anonymous=True, disable_signals=True)
    client = actionlib.SimpleActionClient('follow_joint_trajectory', FollowJointTrajectoryAction)
    print ("Waiting for server...")
    client.wait_for_server()
    print ("Connected to server")
    rate=rospy.Rate(10)

    # Define the subscriber for the robot command
    rospy.Subscriber("/full_robot_command",Float32MultiArray, full_robot_command_callback, queue_size=1)
    # Define the subscriber for the arm's current joint state
    rospy.Subscriber("/joint_states", JointState, arm_state_callback, queue_size=1)

    while not rospy.is_shutdown():
        try:
            # Wait until we get a message on the robot_command topic and get the command
            rospy.wait_for_message('/robot_command',Float32MultiArray,timeout=TIMEOUT)
        except:
            print ('timed out waiting for message on the robot command topic')

        try:
            # Get the current arm joint state
            while rospy.is_shutdown():
                possible_state = rospy.wait_for_message('/joint_states', JointState, timeout=TIMEOUT)
                    if possible_state.name == JOINT_NAMES:
                        print ('Arm joint state received')
                        break
        except:
            print ('timed out waiting for joint state topic')

        print ('received command is', command)

        DURATION = 5
        command_state = robot_state.copy()
        command_state[0] = command[0].copy()
        #control_arm(robot_state, command_state)
        print ('Command {} executed'.format(command))

        rate.sleep()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        rospy.signal_shutdown("KeyboardInterrupt")
        raise
