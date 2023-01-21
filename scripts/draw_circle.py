#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist

if __name__ == '__main__':
    rospy.init_node("draw_circle")
    rospy.loginfo("Node has been started!")

    pub = rospy.Publisher("/turtle1/cmd_vel", Twist, queue_size=10)
    
    rate = rospy.Rate(2)

    while not rospy.is_shutdown():

        #create msg
        msg = Twist()
        msg.linear.x = 2.0

        msg.angular.z = 1.0
        
        #publish the msg
        pub.publish(msg)

        #redo in 2Hz
        rate.sleep() 

