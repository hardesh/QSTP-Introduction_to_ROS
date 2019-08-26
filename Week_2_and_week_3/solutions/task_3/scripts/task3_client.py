#! /usr/bin/env python
import rospy, time, actionlib
from task_3.msg import String_task3Action, String_task3Goal, String_task3Result, String_task3Feedback

rospy.init_node("task3_client")

class Client():
    def __init__(self):
        self.seq_a = ""
        self.client=actionlib.SimpleActionClient("task_3", String_task3Action)
        self.result = String_task3Result()
        self.goal = String_task3Goal()
        self.feedback = String_task3Feedback()

    def get_seq_a(self):
        """Getting sequence A"""
        self.seq_a=raw_input("Give sequence A:")

    def feedback_cb(self, fb):
        """Feedback callback"""
        self.feedback=fb
        print("[FEEDBACK] string typed: {0:20}\tlength of string:{1:2d}".format(self.feedback.string_typed,self.feedback.string_len))
        
    def send_goal(self):
        self.client.wait_for_server()
        self.goal.stop_sequence_A=self.seq_a
        self.client.send_goal(self.goal, feedback_cb=self.feedback_cb)
        self.client.wait_for_result()
        
        self.print_result()

    def print_result(self):
        print('[Result] State: %d'%(self.client.get_state()))
        print('[Result] Status: %s'%(self.client.get_goal_status_text()))
        print('[Result] Time elapsed: %f'%(self.client.get_result().time_elapsed.to_sec()))
        print('[Result] Updates sent: %d'%(self.client.get_result().updates_sent))


        
if __name__=="__main__":
    o=Client()
    o.get_seq_a()
    o.send_goal()    

