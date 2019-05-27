#!/usr/bin/env python 

import rospy
import struct
from sensor_msgs import point_cloud2
from sensor_msgs.msg import PointCloud2, PointField
from std_msgs.msg import Header

rospy.init_node("create_cloud_xyzrgb")
pub = rospy.Publisher("point_cloud_2", PointCloud2, queue_size=10)

position = [0.5, 0.5, 0.5, 1.0, 1.0, 1.0, 1.5, 1.5, 1.5, 2.0, 2.0, 2.0]
#rgb_array = [255,100,100,50,150,100,200,25,200,255,100,255]
points = []
lim = 4

for i in range(lim):
            x = float(position[i*3+0])
            y = float(position[i*3+1])
            z = float(position[i*3+2])
           # r = int(rgb_array[i*3+0])
           # g = int(rgb_array[i*3+1])
           # b = int(rgb_array[i*3+2])
            #a = 255
    
           # rgb = struct.unpack('I', struct.pack('BBBB', b, g, r, a))[0]
            #print hex(rgb)
            pt = [x,y,z] #,rgb]
            points.append(pt)

fields = [
            PointField('x', 0, PointField.FLOAT32, 1),
            PointField('y', 4, PointField.FLOAT32, 1),
            PointField('z', 8, PointField.FLOAT32, 1) #,
            #PointField('rgb', 12, PointField.FLOAT32, 1)
        ]

header = Header()
header.stamp = rospy.Time.now()
header.frame_id = "odom"
pc2 = point_cloud2.create_cloud(header, fields, points)

while not rospy.is_shutdown():
    pc2.header.stamp = rospy.Time.now()
    pub.publish(pc2)
    rospy.sleep(1.0)

