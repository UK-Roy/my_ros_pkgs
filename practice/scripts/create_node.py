#! /usr/bin/env python3

import rospy

rospy.init_node('first_node')
rate = rospy.Rate(2)
while not rospy.is_shutdown():
    print("This is my FIRST ever ROS node")
    rate.sleep()
