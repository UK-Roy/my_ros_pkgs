#!/usr/bin/env python3
from __future__ import print_function

import rospy
from make_shape.srv import *

def circle_client(s):
    rospy.wait_for_service('drawing_circle')
    try:
        make_cir = rospy.ServiceProxy('drawing_circle', Circle)
        resp = make_cir(s)
        return resp.s, resp.x, resp.y, resp.z, resp.w
    except rospy.ServiceException as e:
        print("Service call failed: %s"%e)

if __name__ == "__main__":

    data = circle_client("Lets start Circle")
    print(f"Status: {data[0]}\nOrientation:\nx: {data[1]}\ny: {data[2]}\nz: {data[3]}\nw: {data[4]}")
