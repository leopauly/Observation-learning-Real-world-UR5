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
import control_sequences
JOINT_NAMES = ['shoulder_pan_joint', 'shoulder_lift_joint', 'elbow_joint',
               'wrist_1_joint', 'wrist_2_joint', 'wrist_3_joint']

client = None
#robot_state=[2.353630304336548, -2.0751612822162073, 1.6407523155212402, 6.2166523933410645, 1.6388124227523804, 3.0517871379852295]
#home=[2.353630304336548, -2.0751612822162073, 1.6407523155212402, 6.2166523933410645, 1.6388124227523804, 3.0517871379852295]
#home=[0.02595558390021324, -1.3735793272601526, 1.9524388313293457, 5.7050395011901855, 1.4384504556655884, 3.119882583618164]
#home=[0.07440518587827682, -0.7673614660846155, 1.1787137985229492, -0.25572044054140264, 0.3366859555244446, -3.3494518438922327]
#robot_state=[1.5122687816619873, -0.10656911531557256, 0.07706737518310547, 0.042214393615722656, 1.5209097862243652, 3.190107822418213]
#home=[1.5122687816619873, -0.10656911531557256, 0.07706737518310547, 0.042214393615722656, 1.5209097862243652, 3.190107822418213]
home = control_sequences.home
#home= [-0.7448108831988733, -3.0841191450702112, -0.004925552998678029, -3.192338768635885, -1.5696294943438929, -0.031188789998189748]


# hammer task final pos of initial sequence
#final =  [-0.7590788046466272, -3.060802761708395, -0.003823105488912404, -3.303108040486471, -1.1523990789996546, -0.03758889833559209]
#push taks final pos of initail sequence
final =[-0.5399153868304651, -3.0495827833758753, -0.005501095448629201, -3.2901514212237757, -1.5667222181903284, -0.030637089406148732]


command = np.array([home, 0.])

TIMEOUT=20000 # Waiting for messages
DURATION=0.5 # This is the control duration
CST_DONE=np.zeros(2)# Handshake code

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
    """Checks for state safety on the real robot

    Args:
        command_state: Desired state [state_vec]
    """
    count_unsafe = 0
    ang_diff = 0.1
    num = 8
    JOINT_0l_THRESH = - 0.75 - (num*ang_diff)
    JOINT_1l_THRESH = -3.1  - (ang_diff)
    JOINT_2l_THRESH = -0.007 - (ang_diff)
    JOINT_3l_THRESH = -3.4 - (ang_diff)
    JOINT_4l_THRESH = -1.6 - (num*ang_diff)
    JOINT_5l_THRESH = -0.035 - (ang_diff)

    JOINT_0h_THRESH = - 0.75 + num*ang_diff
    JOINT_1h_THRESH = -3.1 + ang_diff
    JOINT_2h_THRESH = -0.007 + ang_diff
    JOINT_3h_THRESH = -3.4 + ang_diff
    JOINT_4h_THRESH = -1.6 + num*ang_diff
    JOINT_5h_THRESH = -0.035 + ang_diff

    if command_state[0] < JOINT_0l_THRESH or command_state[0] > JOINT_0h_THRESH:
        print ("Input for joint 0 is not safe!")
        count_unsafe += 1

    if command_state[1] < JOINT_1l_THRESH or command_state[1] > JOINT_1h_THRESH:
        print ("Input for joint 1 is not safe!")
        count_unsafe += 1

    if command_state[2] < JOINT_2l_THRESH or command_state[2] > JOINT_2h_THRESH:
        print ("Input for joint 2 is not safe!")
        count_unsafe += 1
    print (command_state[3])
    if command_state[3] < JOINT_3l_THRESH or command_state[3] < JOINT_3h_THRESH:
        print ("Input for joint 3 is not safe!")
        count_unsafe += 1

    if command_state[4] < JOINT_4l_THRESH or command_state[4] > JOINT_4h_THRESH:
        print ("Input for joint 4 is not safe!")
        count_unsafe += 1

    if command_state[5] < JOINT_5l_THRESH or command_state[5] > JOINT_5h_THRESH:
        print ("Input for joint 5 is not safe!")
        count_unsafe += 1


    if count_unsafe > 0:
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
        rate=rospy.Rate(50) # Loop rate of 10 hertz

        # Define the subscriber for the robot command
        rospy.Subscriber("/robot_command",Float32MultiArray, callback_command,queue_size=1)
        # Define the subscriber for the robot's current joint state
        rospy.Subscriber("/joint_states",JointState, callback_state,queue_size=10)
        # Define the publisher for the handshake
        robot_done_pub=rospy.Publisher('/robot_done',numpy_msg(Floats),queue_size=1)

        while not rospy.is_shutdown():
            try:
                # Wait untill we get a message on the robot_command topic and get the command
                rospy.wait_for_message('/robot_command',Float32MultiArray, timeout=TIMEOUT)
            except:
                print ('timed out waiting for message on the robot command topic')

            try:
                # Get the current joint state
                rospy.wait_for_message('/joint_states',JointState,timeout=TIMEOUT)
            except:
                print ('timed out waiting for joint state topic')


            #command[0]=home.copy()
            #command[1]=0
            #print ('received command is',command[0])
            #print ("Reset command is",command[-1])
            if command[-1]>1:
                # Reset the robot to home position
                print ('Resetting robot.........')
                DURATION=2 # Longer to allow for slower motion of the robot
                move_robot(robot_state,home)
                time.sleep(2)
                robot_done_pub.publish(CST_DONE)
                #print ("Published robot done")

            else:
                # Send the command to learn
                DURATION=2
                command_state=robot_state.copy()
                #command_state[0]=command[0]
                #command_state[1]=command[1]
                command_state[0:6] = command[0:6]
                #command_state = command[0][0:]
                safety_flag=check_state_safety(command_state)
                if safety_flag:
                    move_robot(robot_state,command_state)
                    time.sleep(5)
                    robot_done_pub.publish(CST_DONE)
                    print ('Command {} executed'.format(command[0]))
                else:
                    print ('Desired robot state is not safe')
                    time.sleep(2)
                    robot_done_pub.publish(CST_DONE)
            #command=np.array(command)
            #command[0]=0.
            #command[1]=0.


            #print ('I can hear the robot state', robot_state)

            #rate.sleep()

    except KeyboardInterrupt:
        rospy.signal_shutdown("KeyboardInterrupt")
        raise

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        rospy.signal_shutdown("KeyboardInterrupt")
        raise
