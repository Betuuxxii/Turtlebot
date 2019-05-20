#! /usr/bin/env python

import rospy
from std_srvs.srv import Empty, EmptyRequest

# initializing the node
rospy.init_node("disperse_particles")

rospy.wait_for_service("/global_localization")

# create service connection
disperse_particules_service = rospy.ServiceProxy("/global_localization", Empty)
service_msg = EmptyRequest()

result = disperse_particules_service(service_msg)
print result
