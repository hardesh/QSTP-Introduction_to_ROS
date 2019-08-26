#! /usr/bin/env python
import rospy, time, actionlib
from task_3.msg import String_task3Action, String_task3Goal, String_task3Result, String_task3Feedback

rospy.init_node("task3_server")

class Server():
    def __init__(self):
        self.server=actionlib.SimpleActionServer("task_3", String_task3Action, self.server_callback, False)
        self.result = String_task3Result()
        self.goal = String_task3Goal()
        self.feedback = String_task3Feedback()
        self.server_ip=""
        self.seq_a=""
        self.start_time=0.0
        self.updates_sent=0

    def start_server(self):
        self.server.start()
        print("Done start_server")

    def server_callback(self, goal):
        # print("in cb")
        self.goal=goal
        self.seq_a=self.goal.stop_sequence_A
        self.start_time=time.time()

        if len(self.seq_a) > 8:
            self.abort()
            return
    
        while True:
            self.server_ip=raw_input("Give input:")

            if self.server_ip==self.seq_a:
                break            
            
            self.send_feedback()
            self.updates_sent+=1

        self.result.time_elapsed=rospy.Duration.from_sec(time.time()-self.start_time)
        self.result.updates_sent=self.updates_sent
        self.server.set_succeeded(self.result, "Completed Successfully")
        self.updates_sent=0
        return

    def send_feedback(self):
        """Sending Feedback"""
        self.feedback.string_typed=self.server_ip
        self.feedback.string_len=len(self.server_ip)
        self.server.publish_feedback(self.feedback) 

    def abort(self):
        """On reaching Abort condition"""
        self.result.time_elapsed=rospy.Duration.from_sec(time.time()-self.start_time)
        self.result.updates_sent=self.updates_sent
        self.server.set_aborted(self.result, "Aborted!")
        return

    def preempt(self):
        """On reaching Preempt condn"""
        self.result.time_elapsed=rospy.Duration.from_sec(time.time()-self.start_time)
        self.result.updates_sent=self.updates_sent
        self.server.set_preempted(self.result, "Preempted!")
        self.updates_sent=0
        return


if __name__=="__main__":
    o=Server()
    o.start_server()
    rospy.spin()
