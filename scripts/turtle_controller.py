#!/usr/bin/env python3

import rospy

from geometry_msgs.msg import Twist

from turtlesim.msg import Pose

from turtlesim.srv import SetPen       

def call_set_pen_service(r, g, b, width, off):
    try:
        set_pen = rospy.ServiceProxy("/turtle1/set_pen", SetPen)
        response = set_pen(r, g, b, width, off)
        rospy.loginfo(response)

    except rospy.ServiceException as e:
        rospy.logerr(e)


previous_x = 0

def pose_callback(msg: Pose):
    cmd = Twist()

    if msg.x > 8.0 or msg.x < 2.0 or msg.y > 8 or msg.y < 2:
        cmd.linear.x = 1
        cmd.angular.z = 5

    else:
        cmd.linear.x = 3.0
        cmd.linear.y = 0.0
        cmd.angular.z = 0.0

    pub.publish(cmd)

    global previous_x

    # Service shouldn't be called frequently, so we design to call it when really needed
    if msg.x >= 5.5 and previous_x < 5.5:
        call_set_pen_service(240, 23, 42, 2, 0)
        rospy.loginfo("Just moved to the right side of the screen. Color changed.")
    elif msg.x < 5.5 and previous_x >= 5.5:
        call_set_pen_service(42, 23, 24, 2, 0)
        rospy.loginfo("Just moved to the left side of the screen. Color changed.")

    previous_x = msg.x

    
if __name__ == '__main__':
    rospy.init_node("turtule_controller")

    rospy.wait_for_service("/turtle1/set_pen")

    ## Test if the service is working
    # call_set_pen_service(255, 0, 0, 3, 0)


    #create publisher before the subscriber
    pub = rospy.Publisher("/turtle1/cmd_vel", Twist, queue_size=10)

    sub = rospy.Subscriber("/turtle1/pose", Pose,  callback=pose_callback)

    rospy.loginfo("Node (subscriber) has been started.")
    rospy.spin()

