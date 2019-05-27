#!/usr/bin/env python 

import rospy
from visualization_msgs.msg import Marker, MarkerArray

rospy.init_node("marker_array_test")
pub = rospy.Publisher("marker_topic", MarkerArray, queue_size=2)

markerArray = MarkerArray()

position_array = [0.5,0.5,0.5,0.5,0.5,0.6,0.5,0.5,0.7,0.5,0.5,0.8,0.5,0.5,0.9,0.5,0.5,1.0]
while not rospy.is_shutdown():


    for i in range(6):

        marker = Marker()
        marker.header.frame_id = "map"
        marker.type = marker.CUBE
        marker.action = marker.ADD
        marker.scale.x = 0.05
        marker.scale.y = 0.05
        marker.scale.z = 0.05
        marker.color.a = 1.0
        marker.color.r = 1.0
        marker.color.g = 1.0
        marker.color.b = 0.0
        marker.pose.orientation.w = 1.0
        marker.pose.position.x = position_array[i*3+0]
        marker.pose.position.y = position_array[i*3+1] 
        marker.pose.position.z = position_array[i*3+2] 
        marker.id = i+1
        markerArray.markers.append(marker)
        
    pub.publish(markerArray)

    rospy.sleep(0.01)
