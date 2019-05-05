#!/usr/bin/env python 

import rospy
from sensor_msgs.msg import PointCloud2
from sensor_msgs import point_cloud2
from visualization_msgs.msg import Marker, MarkerArray


pub = rospy.Publisher("merged_occupied_cells_array", MarkerArray, queue_size=2)

def visulize_points(points_msg):
    points_translated = []
    i=0
    print "points count: ",points_msg.width
    for p in point_cloud2.read_points(points_msg, skip_nans=True):
        x_translated = round(p[0],3) + 2.000
        y_translated = round(p[1],3)
        z_translated = round(p[2],3)
        pt = [x_translated, y_translated, z_translated]
        points_translated.append(pt)
        i+=1
    fields = [
            PointField('x', 0, PointField.FLOAT32, 1),
            PointField('y', 4, PointField.FLOAT32, 1),
            PointField('z', 8, PointField.FLOAT32, 1) 
        ]

    header = Header()
    header.stamp = rospy.Time.now()
    header.frame_id = "map"
    pc2 = point_cloud2.create_cloud(header, fields, points_translated)
    pub.publish(pc2)

if __name__ == "__main__":
    rospy.init_node('visualize_merged_octomap', anonymous=True)
    rospy.Subscriber('centers_transformed', PointCloud2, transform_points)
    rospy.sleep(1.0)
    rospy.spin()