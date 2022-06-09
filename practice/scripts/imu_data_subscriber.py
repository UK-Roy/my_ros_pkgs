#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import Imu

def callback(data):
    rospy.loginfo(f"\nlinear acceleration:\nx= {data.linear_acceleration.x}\ny= {data.linear_acceleration.y}\nz= {data.linear_acceleration.z}")


def listener():
    rospy.init_node('imu_data_subscriber', anonymous=True)
    rospy.Subscriber('/imu', Imu, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()
    
