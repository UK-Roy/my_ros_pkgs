#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Imu
from make_shape.srv import Circle, CircleResponse

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

def get_imu(data):
    global x, y, z, w

    x = data.orientation.x
    y = data.orientation.y
    z = data.orientation.z
    w = data.orientation.w

def circle(req):
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    sub = rospy.Subscriber('/imu', Imu, get_imu)
    
    print(req.a)
    print(f"Radius")
    twist = Twist()
    stop(twist, pub)
    move(twist, pub)
    rotate(twist, pub)
    print("Now its rotating ........")
    twist.linear.x = 0.1; twist.linear.y = 0.0; twist.linear.z = 0.0
    twist.angular.x = 0.0; twist.angular.y = 0.0; twist.angular.z = 0.1
    pub.publish(twist)
    rospy.sleep(63)
    stop(twist, pub)
    print("The rotation is being completed\nAnd the IMU data is sent through feedback")

    return CircleResponse("Done", x, y, z, w) 

def circle_server():
    rospy.init_node('circle_server')
    rospy.Rate(10).sleep()
    s = rospy.Service('drawing_circle', Circle, circle)
    rospy.spin()

if __name__ == '__main__':
    try:
        circle_server()
    except rospy.ROSInterruptException:
        pass
