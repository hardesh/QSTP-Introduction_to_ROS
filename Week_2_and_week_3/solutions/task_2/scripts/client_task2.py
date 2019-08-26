#! /usr/bin/env python
import rospy
import sys
from task_2.srv import Task2_add, Task2_addRequest , Task2_addResponse

rospy.init_node("client_task2", anonymous=True)

class Client_t2():
    def __init__(self):
        self.client=rospy.ServiceProxy("opt_two_nos", Task2_add)
        self.response=Task2_addResponse()
        self.request=Task2_addRequest()
        self.request.fl1=float(sys.argv[1])
        self.request.fl2=float(sys.argv[2])
        self.request.int_opt=int(sys.argv[3])

    def get_response(self):
        print(sys.argv[0])
        self.response=self.client(self.request)
        print(self.response)

if __name__=="__main__":
    rospy.wait_for_service("opt_two_nos")
    o=Client_t2()
    o.get_response()
    