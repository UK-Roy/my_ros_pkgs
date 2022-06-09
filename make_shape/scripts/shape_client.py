#! /usr/bin/env python3

import rospy
import sys
from make_shape.srv import *

def shape_client(num, shape):
    rospy.wait_for_service('drawing_a_shape')
    try:
        follow_shape = rospy.ServiceProxy('drawing_a_shape', Shape)
        res = follow_shape(num, shape)
        return res.s, res.x, res.y, res.z, res.w
    except rospy.ServiceException as e:
        print("Service call failed: %s"%e)

if __name__ == "__main__":
    if len(sys.argv) == 3:
        shape = sys.argv[1]
        num = int(sys.argv[2])
    else:
        print("%s [x y]"%sys.argv[0])
        sys.exit(1)
    
    data = shape_client(num, shape)
    print(f"Status: {data[0]}\nFinal Pos:\nx: {data[1]}\ny: {data[2]}\nz: {data[3]}\nw: {data[4]}")
