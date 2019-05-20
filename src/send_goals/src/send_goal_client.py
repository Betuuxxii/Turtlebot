#! /usr/bin/env python
import rospy
import time
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal, MoveBaseResult, MoveBaseFeedback

# definition of the feedback callback. This will be called when feedback
# is received from the action server
# it just prints a message indicating a new message has been received


def feedback_callback(feedback):

    print('[Feedback] Going to Goal Pose...')


# initializes the action client node
rospy.init_node('move_base_action_client')

# create the connection to the action server
client = actionlib.SimpleActionClient('/move_base', MoveBaseAction)
# waits until the action server is up and running
client.wait_for_server()

# creates first goal to send to the action server
first_goal = MoveBaseGoal()
first_goal.target_pose.header.frame_id = 'map'
first_goal.target_pose.pose.position.x = 3.60844672552
first_goal.target_pose.pose.position.y = -1.45464817269
first_goal.target_pose.pose.position.z = 0.0
first_goal.target_pose.pose.orientation.x = 0.0
first_goal.target_pose.pose.orientation.y = 0.0
first_goal.target_pose.pose.orientation.z = 0.772024234642
first_goal.target_pose.pose.orientation.w = 0.635593093988


# creates a goal to send to the action server
second_goal = MoveBaseGoal()
second_goal.target_pose.header.frame_id = 'map'
second_goal.target_pose.pose.position.x = -1.30043910146
second_goal.target_pose.pose.position.y = 0.535183712689
second_goal.target_pose.pose.position.z = 0.0
second_goal.target_pose.pose.orientation.x = 0.0
second_goal.target_pose.pose.orientation.y = 0.0
second_goal.target_pose.pose.orientation.z = -0.104122490936
second_goal.target_pose.pose.orientation.w = 0.994564481007


# creates a goal to send to the action server
third_goal = MoveBaseGoal()
third_goal.target_pose.header.frame_id = 'map'
third_goal.target_pose.pose.position.x = 1.4300461008
third_goal.target_pose.pose.position.y = 4.40505645475
third_goal.target_pose.pose.position.z = 0.0
third_goal.target_pose.pose.orientation.x = 0.0
third_goal.target_pose.pose.orientation.y = 0.0
third_goal.target_pose.pose.orientation.z = 0.626667325347
third_goal.target_pose.pose.orientation.w = 0.779286894117


while (True):
    # sends the goal to the action server, specifying which feedback function
    # to call when feedback received
    client.send_goal(first_goal, feedback_cb=feedback_callback)

    # Uncomment these lines to test goal preemption:
    # time.sleep(3.0)
    # client.cancel_goal()  # would cancel the goal 3 seconds after starting

    # wait until the result is obtained
    # you can do other stuff here instead of waiting
    # and check for status from time to time
    # status = client.get_state()
    # check the client API link below for more info

    client.wait_for_result()

    client.send_goal(second_goal, feedback_cb=feedback_callback)

    client.wait_for_result()

    client.send_goal(third_goal, feedback_cb=feedback_callback)

    client.wait_for_result()


    print('[Result] State: %d' % (client.get_state()))
