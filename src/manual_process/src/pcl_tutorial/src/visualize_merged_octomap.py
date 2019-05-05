#!/usr/bin/env python 

import rospy
from sensor_msgs.msg import PointCloud2
from sensor_msgs import point_cloud2
from visualization_msgs.msg import Marker, MarkerArray


pub = rospy.Publisher("merged_occupied_cells_array", MarkerArray, queue_size=2)

def visulize_points(points_msg):
    markerArray = MarkerArray()
    i=0
    for p in point_cloud2.read_points(points_msg, skip_nans=True):
        x_position = p[0]   #extract position data from the point cloud
        y_position = p[1]
        z_position = p[2]

        marker = Marker()
        marker.header.frame_id = "world"
        marker.type = marker.CUBE
        marker.action = marker.ADD
        marker.scale.x = 0.03
        marker.scale.y = 0.03
        marker.scale.z = 0.03
        marker.color.a = 1.0
        marker.color.r = 1.0
        marker.color.g = 1.0
        marker.color.b = 1.0
        marker.pose.orientation.w = 1.0
        marker.pose.position.x = x_position
        marker.pose.position.y = y_position
        marker.pose.position.z = z_position
        marker.id = i+1
        markerArray.markers.append(marker)
        i+=1
    
    pub.publish(markerArray)

if __name__ == "__main__":
    rospy.init_node('visualize_merged_octomap', anonymous=True)
    rospy.Subscriber('octomap_centers_transformed', PointCloud2, visulize_points)
    rospy.sleep(1.0)
    rospy.spin()