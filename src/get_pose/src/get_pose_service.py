#! /usr/bin/env python

import rospy
from geometry_msgs.msg import PoseWithCovarianceStamped, Pose
from std_srvs.srv import Empty, EmptyResponse


robot_pose = Pose()


def service_callback(request):
    """ this function is called when the user calls the service
    /get_pose_service
    @params:
        request: is the message passed to the service
    """

    print "Robot Pose"
    print robot_pose
    return EmptyResponse()


def subscribe_callback(msg):
    """ This function is called when ever the robot published
    to the /amcl_pose topic
    """
    global robot_pose

    robot_pose = msg.pose.pose


rospy.init_node("service_server")  # initializing the node

service_request = rospy.Service(
    "/get_pose_service", Empty, service_callback)  # creating a service

sub_pose = rospy.Subscriber(
    '/amcl_pose', PoseWithCovarianceStamped, subscribe_callback)

rospy.spin()
