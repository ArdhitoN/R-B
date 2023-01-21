#!/usr/bin/env python3

import rospy
from turtlesim.msg import Pose

def pose_callback(msg: Pose):
    rospy.loginfo(f"(x, y): ({msg.x}, {msg.y})")


if __name__ == '__main__':
    
    ##Initialize node
    rospy.init_node("turtle_pose_subscriber")


    sub = rospy.Subscriber("/turtle1/pose", Pose, callback=pose_callback)

    rospy.loginfo("Subscriber active.")
    rospy.spin()
