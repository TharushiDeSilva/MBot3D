#!/usr/bin/env python

import rospy
#import pcl
from sensor_msgs.msg import PointCloud2, PointField
#import sensor_msgs.point_cloud2 as pc2 
#import ros_numpy

def raw_points_cb(msg):
    print msg.width
    print msg.height
    print "\n"
    print "\n"


if __name__ == "__main__":
    rospy.init_node('point_cloud_data', anonymous=True)
    rospy.Subscriber('octomap_point_cloud_centers', PointCloud2, raw_points_cb)
    #rospy.Subscriber('/rtabmap/cloud_map', PointCloud2, raw_points_cb)
    rospy.sleep(1)
    rospy.spin()