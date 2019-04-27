#!/usr/bin/env python

import rospy
#import pcl
from sensor_msgs.msg import PointCloud2
#import sensor_msgs.point_cloud2 as pc2 
#import ros_numpy

def raw_points_cb(msg):
    print msg.fields
    print "\n"


if __name__ == "__main__":
    rospy.init_node('point_cloud_data', anonymous=True)
    rospy.Subscriber('camera/depth/points', PointCloud2, raw_points_cb)
    rospy.spin()