#!/usr/bin/env python

import rospy
from std_msgs.msg import String

rospy.init_node("task_1_sub",anonymous=True)

class Subscriber():
    def __init__(self):
        self.sub=rospy.Subscriber("task1_bus", String, self.print_string)

    def print_string(self, pub_string):
        rospy.loginfo("Data from task1_bus topic: "+"%s", pub_string.data)      

if __name__ == "__main__":
    o=Subscriber()
    rospy.spin()


