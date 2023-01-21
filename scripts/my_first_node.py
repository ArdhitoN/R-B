#!/usr/bin/env python3

import rospy

if __name__ == '__main__':
    ##Initialize node
    rospy.init_node("test_node")

    ## Show log (print out something)
    # rospy.loginfo("Hello from test node")
    
    ## Show warn-log 
    # rospy.logwarn("This is a warning")
    
    ## Show error-log 
    # rospy.logerr("This is an error msg")

    ## Wait for 1 sec
    # rospy.sleep(1)

    # Error, because we can't add space for the name of the node
    # rospy.init_node("test node")
    
    rospy.loginfo("Test node has been started.")

    rate = rospy.Rate(10)

    while not rospy.is_shutdown():
        rospy.loginfo("Hello")
        rate.sleep()

