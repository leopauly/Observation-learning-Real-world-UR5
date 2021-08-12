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
command = np.array([0.0,0.0])
#robot_state=[2.353630304336548, -2.0751612822162073, 1.6407523155212402, 6.2166523933410645, 1.6388124227523804, 3.0517871379852295]
#home=[2.353630304336548, -2.0751612822162073, 1.6407523155212402, 6.2166523933410645, 1.6388124227523804, 3.0517871379852295]
#home=[0.02595558390021324, -1.3735793272601526, 1.9524388313293457, 5.7050395011901855, 1.4384504556655884, 3.119882583618164]
#home=[0.07440518587827682, -0.7673614660846155, 1.1787137985229492, -0.25572044054140264, 0.3366859555244446, -3.3494518438922327]
robot_state=[1.5122687816619873, -0.10656911531557256, 0.07706737518310547, 0.042214393615722656, 1.5209097862243652, 3.190107822418213]
home=[1.5122687816619873, -0.10656911531557256, 0.07706737518310547, 0.042214393615722656, 1.5209097862243652, 3.190107822418213]

TIMEOUT=2000 # Waiting for messages
DURATION=2 # This is the control duration
CST_DONE=np.zeros(2)# Handshake code
JOINT_LIMIT=4
JOINT_LIMIT_3=6.5
def callback_command(data):
    global command
    command=data.data

def callback_state(data):
    global robot_state
    robot_state=np.array(data.position)

def move_robot(current_state,desired_state):
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

def check_state_safety(command_state):
    count_negative=0
    for k in range(command_state.shape[0]):
        #print (k)
        if (command_state[k] > JOINT_LIMIT or command_state[k] < -JOINT_LIMIT) and k!=3:
            # Joint limit reached
            print ('Joint limit reached',command_state[k])
            count_negative+=1

        if (command_state[k] > JOINT_LIMIT_3 or command_state[k] < -JOINT_LIMIT_3 )and k==3:
            # Joint limit on joint 3 reached
            print ('Joint 3 limit reached')
            count_negative+=1

    if count_negative>0:
        return False
    else:
        return True

def main():
    global client
    global command
    global robot_state
    global TIMEOUT
    global DURATION
    try:
        rospy.init_node("robot_node", anonymous=True, disable_signals=True)
        client = actionlib.SimpleActionClient('follow_joint_trajectory', FollowJointTrajectoryAction)
        print "Waiting for server..."
        client.wait_for_server()
        print "Connected to server"
        rate=rospy.Rate(10) # Loop rate of 10 hertz

        # Define the subscriber for the robot command
        rospy.Subscriber("/robot_command",Float32MultiArray, callback_command,queue_size=1)
        # Define the subscriber for the robot's current joint state
        rospy.Subscriber("/joint_states",JointState, callback_state,queue_size=1)
        # Define the publisher for the handshake
        robot_done_pub=rospy.Publisher('robot_done',numpy_msg(Floats),queue_size=1)

        while not rospy.is_shutdown():

            """
            try:
                # Wait untill we get a message on the robot_command topic and get the command
                rospy.wait_for_message('/robot_command',Float32MultiArray,timeout=TIMEOUT)
            except:
                print ('timed out waiting for message on the robot command topic')
            """

            try:
                # Get the current joint state
                rospy.wait_for_message('/joint_states',JointState,timeout=TIMEOUT)
            except:
                print ('timed out waiting for joint state topic')

            #
            command[0]=-0.25
            command[1]=100
            print ('received command is',command[0])
            if command[1]>1:
                # Reset the robot to home position
                print ('Resetting robot.........')
                DURATION=5 # Longer to allow for slower motion of the robot
                #move_robot(robot_state,home)
                robot_done_pub.publish(CST_DONE)


            else:
                # Send the command to learn
                DURATION=5
                command_state=robot_state.copy()
                command_state[0]=command[0]
                safety_flag=check_state_safety(command_state)
                if safety_flag:
                    #move_robot(robot_state,command_state)
                    robot_done_pub.publish(CST_DONE)
                    print ('Command {} executed'.format(command[0]))
                else:
                    print ('Desired robot state is not safe')
            command=np.array(command)
            command[0]=0.
            command[1]=0.


            #print ('I can hear the robot state', robot_state)

            rate.sleep()

    except KeyboardInterrupt:
        rospy.signal_shutdown("KeyboardInterrupt")
        raise

if __name__ == '__main__':
    main()
