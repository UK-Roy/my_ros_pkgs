#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist

def stop(twist, pub):
    twist.linear.x = 0.0; twist.linear.y = 0.0; twist.linear.z = 0.0
    twist.angular.x = 0.0; twist.angular.y = 0.0; twist.angular.z = 0.0
    pub.publish(twist)
    rospy.sleep(1)

def rotate(twist, pub):
        twist.linear.x = 0.0; twist.linear.y = 0.0; twist.linear.z = 0.0
        twist.angular.x = 0.0; twist.angular.y = 0.0; twist.angular.z = 0.1
        pub.publish(twist)
        rospy.sleep(16)
        stop(twist, pub)

def move(twist, pub):
        twist.linear.x = 0.1; twist.linear.y = 0.0; twist.linear.z = 0.0
        twist.angular.x = 0.0; twist.angular.y = 0.0; twist.angular.z = 0.0
        pub.publish(twist)
        rospy.sleep(10)
        stop(twist, pub)

def square():
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    rospy.init_node('square', anonymous=True)
    rospy.Rate(10).sleep()
    
    twist = Twist()
    #stop(twist, pub)
    for i in range(5):
        move(twist, pub)
        #rotate(twist, pub)
        if i != 4:
            rotate(twist, pub)
    
    stop(twist, pub)
 
if __name__ == '__main__':
    try:
        square()
    except rospy.ROSInterruptException:
        pass