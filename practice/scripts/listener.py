#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

def callback(data):
    rospy.loginfo(f" I can hear{data.data} from IHABOT topic") 
    
def listener():
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber("IHABOT", String, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()
