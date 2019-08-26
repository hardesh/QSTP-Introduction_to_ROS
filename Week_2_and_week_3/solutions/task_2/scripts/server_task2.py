#! /usr/bin/env python

import rospy
from task_2.srv import Task2_add, Task2_addRequest, Task2_addResponse

rospy.init_node("server_task2",anonymous=True)

class Service_t2():
    def __init__(self): 
        self.serv=rospy.Service("opt_two_nos", Task2_add, self.compute)
        self.response=Task2_addResponse()
        self.fl1='0.0'
        self.fl2='0.0'
        self.int_opt=0
        self.opt_task=['+','-','*','/']

    def compute(self, request):
        self.fl1=str(request.fl1)
        self.fl2=str(request.fl2)
        self.int_opt=request.int_opt-1
       
        try:
            assert(self.int_opt >= 0)
            operand=self.opt_task[self.int_opt]
            self.response.result=eval(self.fl1+operand+self.fl2)
            self.response.is_valid=True
            return self.response

        except:
            self.response.result=0.0
            self.response.is_valid=False
            return self.response

if __name__=="__main__":
    o=Service_t2()
    rospy.spin()





