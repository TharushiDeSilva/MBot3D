#!/usr/bin/env python

import rospy
from octomap_msgs.msg import Octomap 

def octomap_cb(msg):
     
    print msg.header
    print msg.binary
    print msg.id
    print msg.resolution
    print len(msg.data)
    print "\n"



if __name__ == "__main__":
    rospy.init_node('read_octomap', anonymous=True)
    rospy.Subscriber('octomap_full', Octomap, octomap_cb)
    rospy.spin()