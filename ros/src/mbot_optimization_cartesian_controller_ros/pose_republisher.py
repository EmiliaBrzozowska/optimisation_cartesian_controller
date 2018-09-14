#!/usr/bin/env python

import rospy
from geometry_msgs.msg import PoseStamped
from std_msgs.msg import String

#mbot class
# from mbot_robot_class_ros import mbot as mbot_class

class PoseRepublisher(object):
    def __init__(self):
        # self.mbot = mbot_class.mbotRobot(enabled_components=['yolo'])
        rospy.Subscriber("~event_in", String, self.evenInCallback, queue_size=1)
        rospy.Subscriber("~pose", PoseStamped, self.poseCallback, queue_size=1)
        self.pub_event_out = rospy.Publisher('~event_out', String, queue_size=1)
        self.pub_target_pose = rospy.Publisher('/optimization_cart_ctrler_node/target_pose', PoseStamped, queue_size=1)
        self.start = False
        self.pose = None

        self.loop_rate = rospy.Rate(rospy.get_param('~loop_rate', 10.0))
        rospy.loginfo('[Pose Republisher] node initialized, ready to start')

    def evenInCallback(self, msg):
        if msg.data == 'e_start':
            self.start = True
        elif msg.data == 'e_stop':
            self.start = False

    def poseCallback(self, msg):
        self.pose = msg

    def start_republisher(self):
        '''
        node main loop function
        '''
        while not rospy.is_shutdown():
            if self.start:
                self.pub_event_out.publish(String('e_started'))

                pose = self.pose
                while (self.start):
                    if (pose):
                        pose.header.stamp = rospy.Time.now()
                        self.pub_target_pose.publish(pose)
                    self.loop_rate.sleep()

                self.pub_event_out.publish(String('e_stopped'))

                self.pose = None
            self.loop_rate.sleep()

def main():
    rospy.init_node('pose_republisher', anonymous=False)
    republish = PoseRepublisher()
    try:
        republish.start_republisher()
    except Exception as e:
        self.pub_event_out.publish(String('e_failure'))
        rospy.logerr('[PoseRepublisher] : {}'.format(e))
