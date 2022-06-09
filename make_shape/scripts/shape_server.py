#! /usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
from make_shape.srv import Shape, ShapeResponse
from robot import Robot
from sensor_msgs.msg import Imu

def get_imu(data):
    global x, y, z, w
    x = data.orientation.x
    y = data.orientation.y
    z = data.orientation.z
    w = data.orientation.w

def move(req):

    srot = Robot()
    sub = rospy.Subscriber('/imu', Imu, get_imu, queue_size=10) 
    print(f"Lets follow a {req.shape} for {req.num} times")
    if req.shape == 'circle':
        fb = srot.circle(req.num)
    elif req.shape == 'square':
        fb = srot.square(req.num)
    else:
        print("This shape is not defined")
    sub.unregister()
    srot.resetting_world()
    print("Feedback is sent")
    return ShapeResponse(fb, x, y, z, w)

def shape_server():
    rospy.init_node('shape_server')
    rospy.Rate(10).sleep()
    s = rospy.Service('drawing_a_shape', Shape, move)
    rospy.spin()

if __name__ == '__main__':
    try:
        shape_server()
    except rospy.ROSInterruptException:
        pass
