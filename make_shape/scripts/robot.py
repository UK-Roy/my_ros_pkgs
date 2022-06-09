#! /usr/bin/env python3

from cgitb import reset
import rospy
import sys
from geometry_msgs.msg import Twist
from std_srvs.srv import Empty

class Robot():

    def __init__(self) -> None:
        self.vel_publiser = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
        self.cmd = Twist()
        self.ctrl_c = False
        rospy.Rate(1).sleep()
    
    def resetting_world(self):
        rospy.wait_for_service('/gazebo/reset_world')
        reset_world = rospy.ServiceProxy('/gazebo/reset_world', Empty)
        reset_world()
        
    def stop(self, twist, pub):
        twist.linear.x = 0.0; twist.linear.y = 0.0; twist.linear.z = 0.0
        twist.angular.x = 0.0; twist.angular.y = 0.0; twist.angular.z = 0.0
        pub.publish(twist)
        rospy.sleep(1)

    def rotate(self, twist, pub):
            twist.linear.x = 0.0; twist.linear.y = 0.0; twist.linear.z = 0.0
            twist.angular.x = 0.0; twist.angular.y = 0.0; twist.angular.z = 0.1
            pub.publish(twist)
            rospy.sleep(16)
            self.stop(twist, pub)

    def move(self, twist, pub):
            twist.linear.x = 0.1; twist.linear.y = 0.0; twist.linear.z = 0.0
            twist.angular.x = 0.0; twist.angular.y = 0.0; twist.angular.z = 0.0
            pub.publish(twist)
            rospy.sleep(10)
            self.stop(twist, pub)
    
    def square(self, num):
        for i in range(num):
            print(f"Now its moving for square {i+1}........")
            for j in range(4):
                self.rotate(self.cmd, self.vel_publiser)
                self.move(self.cmd, self.vel_publiser)
            print(f"Square no: {i+1} is done")
        return f"Successfully {num} square is follwed"
    
    def circle(self, num):
        self.move(self.cmd, self.vel_publiser)
        self.rotate(self.cmd, self.vel_publiser)
        for i in range(1*num):
            print(f"Now its rotating for circle {i+1}........")
            self.cmd.linear.x = 0.1; self.cmd.linear.y = 0.0; self.cmd.linear.z = 0.0
            self.cmd.angular.x = 0.0; self.cmd.angular.y = 0.0; self.cmd.angular.z = 0.1
            self.vel_publiser.publish(self.cmd)
            rospy.sleep(63)
            self.stop(self.cmd, self.vel_publiser)
            print(f"Circle no: {i+1} is done")
        return f"Successfully {num} circle is follwed"

if __name__ == "__main__":
    rospy.init_node('Robot_class', anonymous=True)
    if len(sys.argv) == 3:
        shape = sys.argv[1]
        num = int(sys.argv[2])
    else:
        print("%s [x y]"%sys.argv[0])
        sys.exit(1)
    
    arit = Robot()

    if shape == 'circle':
        data = arit.circle(num)
    elif shape == 'square':
        data = arit.square(num)
    else:
        print("This shape is not defined") 
    print(data)
    arit.resetting_world()
