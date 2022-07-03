#!/usr/bin/env python3  
import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from math import radians, degrees
from actionlib_msgs.msg import *
from geometry_msgs.msg import Point




#this method will make the robot move to the goal location
def move_to_goal(xGoal,yGoal):

   #define a client for to send goal requests to the move_base server through a SimpleActionClient
   ac = actionlib.SimpleActionClient("move_base", MoveBaseAction)

   #wait for the action server to come up
   while(not ac.wait_for_server(rospy.Duration.from_sec(5.0))):
           rospy.loginfo("Waiting for the move_base action server to come up")

   goal = MoveBaseGoal()
   
   
   #set up the frame parameters
   goal.target_pose.header.frame_id = "map"
   goal.target_pose.header.stamp = rospy.Time.now()

   # moving towards the goal*/

   goal.target_pose.pose.position =  Point(xGoal,yGoal,0)
   goal.target_pose.pose.orientation.x = 0.0
   goal.target_pose.pose.orientation.y = 0.0
   goal.target_pose.pose.orientation.z = 0.0
   goal.target_pose.pose.orientation.w = 1.0

   rospy.loginfo("Sending goal location ...")
   ac.send_goal(goal)

   ac.wait_for_result(rospy.Duration(60))

   if(ac.get_state() ==  GoalStatus.SUCCEEDED):
           rospy.loginfo("You have reached the destination")
           return True

   else:
           rospy.loginfo("The robot failed to reach the destination")
           return False

if __name__ == '__main__':
   rospy.init_node('map_navigation', anonymous=False)
   x=int(input("please enter table number to deliver to \n"))
   if x == 1 :
        x_goal = 12.9
        y_goal =-2
        
   elif x == 2:
        x_goal= 13.0
        y_goal=-6.57
   elif x==3 :
        x_goal=16.09
        y_goal=-2.06
   elif x==4:
        x_goal=15.96
        y_goal=-6.57
   else:
        print("please enter a valid table number")   

   print('start go to goal')
   move_to_goal(x_goal,y_goal)
   rospy.spin()