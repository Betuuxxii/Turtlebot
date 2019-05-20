#! /usr/bin/env python

""" This is a service client.
The aim of this file is to access the provided map through a service
"""

import rospy
from nav_msgs.srv import GetMap, GetMapRequest


rospy.init_node('map_requester')  # initialise node

# wait for service to be available
rospy.wait_for_service("/static_map")

conn_map_provider = rospy.ServiceProxy("/static_map", GetMap)

map_data = GetMapRequest()
result = conn_map_provider(map_data)
print result
