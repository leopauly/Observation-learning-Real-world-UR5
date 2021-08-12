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
from geometry_msgs.msg import Twist
from robotiq_c_model_control.msg import _CModel_robot_output  as outputMsg
from robotiq_c_model_control.msg import _CModel_robot_input  as inputMsg


JOINT_NAMES = ['shoulder_pan_joint', 'shoulder_lift_joint', 'elbow_joint',
               'wrist_1_joint', 'wrist_2_joint', 'wrist_3_joint']

client = None
TIMEOUT=2000
command = None
CTRL_DUR = 0.2

def full_robot_command_callback(data):
    global command
    command = data.data

def arm_state_callback(data):
    global robot_state
    global arm_state_read

    if data.name == JOINT_NAMES:
        #print ('Yes, this is the arm joint state')
        robot_state = np.array(data.position)
        #print (robot_state)
        arm_state_read = True

def gripper_state_callback(data):
    global gripper_state
    gripper_state = data.gPR

def control_arm(current_state, desired_state):
    g = FollowJointTrajectoryGoal()
    g.trajectory = JointTrajectory()
    g.trajectory.joint_names = JOINT_NAMES
    g.trajectory.points = [
        JointTrajectoryPoint(positions=current_state, velocities=[0]*6, time_from_start=rospy.Duration(0)),
        JointTrajectoryPoint(positions=desired_state, velocities=[0]*6, time_from_start=rospy.Duration(DURATION))]
    client.send_goal(g)
    # try:
    #     client.wait_for_result()
    # except KeyboardInterrupt:
    #     client.cancel_goal()
    #     raise

def control_gripper(gripper_action):

    if gripper_action > 1:
        gripper_action = 1 
    if gripper_action < 0:
	gripper_action = 0 
    # Create gripper command
    gripper_command = outputMsg.CModel_robot_output()
    gripper_command.rACT = 1
    gripper_command.rGTO = 1
    gripper_command.rFR  = 150
    gripper_command.rATR = 0
    if gripper_command.rSP > 255:
        gripper_command.rSP = 255

    gripper_final_state = int(gripper_action*255)
    gripper_initial_state = gripper_state

    # Publish base and gripper commands
    print ("Gripper initial state", gripper_initial_state)
    print ("Gripper final state", gripper_final_state)

    gripper_command.rPR = gripper_final_state
    gripper_command.rSP  = int((gripper_final_state - gripper_initial_state)/float(DURATION*255))
    gripper_pub.publish(gripper_command)

def control_base(base_action):
    # Create base command
    base_command = Twist()

    OVERCOME_FRICTION = 0.98

    #cst_timestep = DURATION
    total_count = int(PUBLISHING_RATE*DURATION)

    vx_command = (base_action[0]/(OVERCOME_FRICTION))*(CTRL_DUR/float(DURATION))
    vy_command = (base_action[1]/(OVERCOME_FRICTION))*(CTRL_DUR/float(DURATION))

    if abs(vy_command) >= VY_MAX :
        vy_command = VY_MAX*np.sign(vy_command)

    if abs(vx_command) >= VX_MAX :
        vx_command = VX_MAX*np.sign(vx_command)

    base_command.linear.x = vx_command
    base_command.linear.y = vy_command
    base_command.angular.z = 0.

    for k in range(total_count):
        base_pub.publish(base_command)
        rate.sleep()

def main():
    global arm_state # The robot's current state
    global TIMEOUT  # Max time to wait for message
    global DURATION # Control duration
    global command  # Full robot command
    global client    # Follow joint trajectory client for the arm
    global arm_state_read
    global base_pub
    global gripper_pub
    global rate
    global PUBLISHING_RATE
    global VX_MAX
    global VY_MAX
    global gripper_state

    DURATION = 4 # The control duration is 5 seconds
    PUBLISHING_RATE = 10
    VX_MAX = 0.2
    VY_MAX = 0.2
    # Initialize the robot node
    rospy.init_node("full_robot_node", anonymous=True, disable_signals=True)
    client = actionlib.SimpleActionClient('follow_joint_trajectory', FollowJointTrajectoryAction)
    print ("Waiting for server...")
    client.wait_for_server()
    print ("Connected to server")
    rate = rospy.Rate(PUBLISHING_RATE)

    # Define the subscriber for the robot command
    rospy.Subscriber("/full_robot_command",Float32MultiArray, full_robot_command_callback, queue_size=1)
    # Define the subscriber for the arm's current joint state
    rospy.Subscriber("/joint_states", JointState, arm_state_callback, queue_size=1)
    # Define subscriber to gripper state
    rospy.Subscriber("/CModelRobotInput", inputMsg.CModel_robot_input, gripper_state_callback, queue_size=1 )
    # Define the the publisher for the base
    base_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
    # Define the gripper publisher
    gripper_pub = rospy.Publisher('CModelRobotOutput', outputMsg.CModel_robot_output, queue_size=1)

    while not rospy.is_shutdown():
        arm_state_read = False

        try:
            # Wait until we get a message on the robot_command topic and get the command
            rospy.wait_for_message('/full_robot_command',Float32MultiArray, timeout=TIMEOUT)
        except:
            print ('timed out waiting for message on the robot command topic')

        if arm_state_read:
            print ('Arm joint state received')
            print (robot_state)

        print ('received command is', command)

        base_action = command[0:3]
        arm_action = command[3:9]
        gripper_action = command[9]

        command_state = robot_state.copy()
        command_state[0:6] = arm_action
        control_arm(robot_state, command_state)
        control_gripper(gripper_action)
        control_base(base_action)


        print ('Command {} executed'.format(command))

        rate.sleep()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        rospy.signal_shutdown("KeyboardInterrupt")
        raise
