#!/usr/bin/env python

import rospy
from std_msgs.msg import String
rospy.init_node("task_1_pub" , anonymous="True")

class Publisher():
    def __init__(self):
        self.pub_string=String() #string to publish
        self.pub=rospy.Publisher("task1_bus", String, queue_size=10)
        self.rate=rospy.Rate(2)

    def take_ip(self):
    # """Takes string input from user and stores"""    
        temp=str(raw_input("Give input string to be published: "))
        self.pub_string.data=temp

    def pub_str_to_topic(self):
    # """Publishes the string to task1_bus"""
        while not rospy.is_shutdown():
            self.pub.publish(self.pub_string)
            rospy.loginfo("Publishing: %s", self.pub_string)
            self.rate.sleep()

if __name__=="__main__":
    o=Publisher()
    o.take_ip()
    o.pub_str_to_topic()
    
        

