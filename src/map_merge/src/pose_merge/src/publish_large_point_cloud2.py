#!/usr/bin/env python 

import rospy
import struct
from sensor_msgs import point_cloud2
from sensor_msgs.msg import PointCloud2, PointField
from std_msgs.msg import Header

rospy.init_node("create_large_octomap_2")
pub2 = rospy.Publisher("octomap_centers", PointCloud2, queue_size=10)
points = []

for x in range(100,200):
    for y in range(100,200):
        for z in range(0,100):
            point_x = float(x/100.00) 
            point_y = float(y/100.00) 
            point_z = float(z/100.00)
            #print point_x, point_y, point_z
            pt = [point_x, point_y, point_z]
            points.append(pt)

fields = [
            PointField('x', 0, PointField.FLOAT32, 1),
            PointField('y', 4, PointField.FLOAT32, 1),
            PointField('z', 8, PointField.FLOAT32, 1) 
        ]

header = Header()
header.stamp = rospy.Time.now()
header.frame_id = "map"
pc2 = point_cloud2.create_cloud(header, fields, points)

while not rospy.is_shutdown():
    pc2.header.stamp = rospy.Time.now()
    pub2.publish(pc2)
    rospy.sleep(1.0)

