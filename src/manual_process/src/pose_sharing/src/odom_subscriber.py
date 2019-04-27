#!/usr/bin/env python
import rospy
from nav_msgs.msg import Odometry

def odometry_cb(msg):
    print msg.pose.pose
    print "\n"


if __name__ == "__main__":
    rospy.init_node('odometry', anonymous=True)
    rospy.Subscriber('odom', Odometry, odometry_cb)
    rospy.spin()