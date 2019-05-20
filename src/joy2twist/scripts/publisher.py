#!/usr/bin/env python

import rospy
from sensor_msgs.msg import Joy
from geometry_msgs.msg import Twist

def callback(data):
    rospy.loginfo(rospy.get_name() +'{}'.format(data.axes))
    
    msg = Twist()

    msg.linear.x=data.axes[1]
    msg.angular.z = data.axes[0]
    pub.publish(msg)

def listener():
    
    global pub
    
    rospy.init_node('joy2twist', anonymous=True)
    
    rospy.Subscriber('/joy',Joy, callback)
    
    #pub = rospy.Publisher('/cmd_vel', Joy, callback, queue_size=10)
    pub = rospy.Publisher('/cmd_vel',Twist, queue_size=10)

    rospy.spin()

if __name__ == '__main__':
    listener()
