#!/usr/bin/env python

import rospy
from geometry_msgs.msg import PoseWithCovarianceStamped
import numpy

def initializer():
    pub = rospy.Publisher('/initialpose', PoseWithCovarianceStamped, queue_size=1)
    rospy.init_node('pose_initializer', anonymous=True)
    robot_pose = PoseWithCovarianceStamped()
    robot_pose.pose.pose.position.x = 1.4300461008
    robot_pose.pose.pose.position.y = 4.40505645475
    robot_pose.pose.pose.position.z = 0.0
    robot_pose.pose.pose.orientation.x = 0.0
    robot_pose.pose.pose.orientation.y = 0.0
    robot_pose.pose.pose.orientation.z = 0.626667325347
    robot_pose.pose.pose.orientation.w = 0.779286894117


    rate = rospy.Rate(10)

    while not rospy.is_shutdown():

        connections = pub.get_num_connections()
        rospy.loginfo('Connections: %d', connections)

        if connections > 0:
            pub.publish(robot_pose)
            break
            rospy.loginfo('Initial Pose Published')

        rate.sleep()

if __name__ == '__main__':

    try:
        initializer()
    except rospy.ROSInterruptException:
        pass
