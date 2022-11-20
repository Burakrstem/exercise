#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import rospy
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist
from math import pow, atan2, sqrt

class MotionController:
    
    def __init__(self):
        rospy.init_node('motioncontroller')
        self.velocity_publisher = rospy.Publisher('/turtle1/cmd_vel',Twist, queue_size=5)
        self.pose_subscriber = rospy.Subscriber('/turtle1/pose',Pose,self.callbackCurrentPose)
        self.goal_pose_subscriber = rospy.Subscriber('/cmd/goal_pose',Pose,self.callbackGoalPose)
        
        self.goal_pose = Pose()
        self.pose = Pose()
        
        self.loop_rate = rospy.Rate(10)
        
    def callbackGoalPose(self,msg):
        self.goal_pose = msg
        
    def callbackCurrentPose(self,msg):
        self.pose = msg
        
    def distance(self):
        return sqrt(pow((self.goal_pose.x - self.pose.x),2)+pow((self.goal_pose.y-self.pose.y),2))
    def linear_vel(self):
        return 1.5*self.distance()
    def angular_vel(self):
        return 6* (atan2(self.goal_pose.y - self.pose.y, self.goal_pose.x - self.pose.x) - self.pose.theta)
    
    def move_goal(self):
        while self.goal_pose_subscriber==None:
            rospy.sleep()
    
        vel_msg = Twist()
        while not rospy.is_shutdown():
            xg=self.goal_pose.x
            yg=self.goal_pose.y
            print("Hedef konum:",xg,yg)

            vel_msg.linear.x = self.linear_vel()
            vel_msg.angular.z = self.angular_vel()
            
            self.velocity_publisher.publish(vel_msg)
            self.loop_rate.sleep()
            
        vel_msg.linear.x = 0
        vel_msg.angular.z = 0
        self.velocity_publisher.publish(vel_msg)
        rospy.spin()
        
if __name__=='__main__':
    x = MotionController()
    x.move_goal()