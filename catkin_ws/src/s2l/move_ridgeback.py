
import rospy
from geometry_msgs.msg import Twist

def move_robot():
    """ This function takes in commands from the user and moves the robot
    """
    base_pub = rospy.Publisher('/cmd_vel',Twist,queue_size=1)
    rospy.init_node('manual_move_node', anonymous=False)
    rate = 20
    r = rospy.Rate(rate)
    parsed_command= Twist()

    scale = 40
    vx_command = 0.001*scale
    vy_command = 0.001*scale
    vz_command = 0.001*scale

    move_robot = False
    while not rospy.is_shutdown():
        print ("True")
        # Get command from the user
        com = raw_input('Command:').split()
        if len(com) == 0:
            print ("No input")
            mmove_robot = False
        elif com[0] == 'a':
            # Move forward
            move_robot = True
            parsed_command.linear.x = 0.
            parsed_command.linear.y = vy_command
            parsed_command.angular.z = 0.
        elif com[0] == "d":
            # Move backward
            move_robot = True
            parsed_command.linear.x = 0.
            parsed_command.linear.y = -vy_command
            parsed_command.angular.z = 0.
        elif com[0] == "s":
            # Move to the left
            move_robot = True
            parsed_command.linear.x = -vx_command
            parsed_command.linear.y = 0.
            parsed_command.angular.z = 0.
        elif com[0] == "w":
            # Move to the right
            move_robot = True
            parsed_command.linear.x = vx_command
            parsed_command.linear.y = 0.
            parsed_command.angular.z = 0.
        elif com[0] == "l":
            # Rotate right
            move_robot = True
            parsed_command.linear.x = 0.
            parsed_command.linear.y = 0.
            parsed_command.angular.z = -vz_command
        elif com[0] == "r":
            # Rotate left
            move_robot = True
            parsed_command.linear.x = 0.
            parsed_command.linear.y = 0.
            parsed_command.angular.z = vz_command

        if move_robot:
            cst_timestep = 1.0
            count = int(rate*cst_timestep)
            for k in range(count):
                base_pub.publish(parsed_command)
                r.sleep()

        #rospy.spin()

if __name__ == "__main__":
    try:
        move_robot()
    except:
        print ("Node shutdown")
