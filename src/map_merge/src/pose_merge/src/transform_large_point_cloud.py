#!/usr/bin/env python 

import rospy
import math
from sensor_msgs.msg import PointCloud2, PointField
from sensor_msgs import point_cloud2
from std_msgs.msg import Header
import time 

robot0_pose = [0, 3.0, 0]     #for individual testing 

pub = rospy.Publisher("octomap_centers_transformed", PointCloud2, queue_size=10)

points_transformed = []

 
def transform_points_robot(points_msg):
   
    start = time.time()
    del points_transformed[:]
    print "delete level", len(points_transformed)

    for p in point_cloud2.read_points(points_msg, skip_nans=True):
        
        z_translated = round(p[2],3)
        if(z_translated<0.00):
            continue
        x_translated = round(p[0],3) + robot0_pose[0]
        y_translated = round(p[1],3) + robot0_pose[1]
        rotation_angle = math.radians(robot0_pose[2])
        x_transformed = x_translated*math.cos(rotation_angle) + y_translated*math.sin(rotation_angle)
        y_transformed = y_translated*math.cos(rotation_angle) - x_translated*math.sin(rotation_angle) 

        pt = [x_transformed, y_transformed, z_translated]
        points_transformed.append(pt)
    
    fields = [PointField('x', 0, PointField.FLOAT32, 1), PointField('y', 4, PointField.FLOAT32, 1),PointField('z', 8, PointField.FLOAT32, 1)]
    header = Header()
    header.stamp = rospy.Time.now()
    header.frame_id = "world"
    pc2 = point_cloud2.create_cloud(header, fields, points_transformed)
    pub.publish(pc2)
    
    duration = time.time() - start
    print "duration", duration
    print "append level", len(points_transformed)


if __name__ == "__main__":
    
    rospy.init_node('transform_cloud', anonymous=True)
    rospy.Subscriber('/octomap_centers', PointCloud2, transform_points_robot)
    rospy.spin()