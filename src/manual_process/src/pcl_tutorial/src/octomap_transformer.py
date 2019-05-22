#!/usr/bin/env python 

import rospy
import math
from sensor_msgs.msg import PointCloud2, PointField
from sensor_msgs import point_cloud2
from std_msgs.msg import Header


# starting pose of robot1 relative to the world 
robot1_pose = [0, 0, 0] # x position, y position, yaw angle in cw  (z position, roll, pitch are constant)    

# Starting pose of robot2 relative to the world
robot2_pose = [0, -2.0, 0]

robot0_pose = [0, 3.0, 0]     #for individual testing 
# This publish topic should be common to all robots
pub = rospy.Publisher("octomap_centers_transformed", PointCloud2, queue_size=2)
#pub2 = rospy.Publisher("octomap_centers_transformed", PointCloud2, queue_size=2)

points_transformed = []

def transform_points_robot1(points_msg):
    #points_transformed = []

    for p in point_cloud2.read_points(points_msg, skip_nans=True):
        x_translated = round(p[0],3) + robot1_pose[0]
        y_translated = round(p[1],3) + robot1_pose[1]
        z_translated = round(p[2],3)
        
       
        rotation_angle = math.radians(robot1_pose[2])
        x_transformed = x_translated*math.cos(rotation_angle) + y_translated*math.sin(rotation_angle)
        y_transformed = y_translated*math.cos(rotation_angle) - x_translated*math.sin(rotation_angle) 

        pt = [x_transformed, y_transformed, z_translated]
        if (z_translated>= 0.00):
            points_transformed.append(pt)
    
    
    fields = [PointField('x', 0, PointField.FLOAT32, 1), PointField('y', 4, PointField.FLOAT32, 1),PointField('z', 8, PointField.FLOAT32, 1)]

    header = Header()
    header.stamp = rospy.Time.now()
    header.frame_id = "world"
    pc2 = point_cloud2.create_cloud(header, fields, points_transformed)
    pub.publish(pc2)

def transform_points_robot2(points_msg):
    #points_transformed = []

    for p in point_cloud2.read_points(points_msg, skip_nans=True):
        x_translated = round(p[0],3) + robot2_pose[0]
        y_translated = round(p[1],3) + robot2_pose[1]
        z_translated = round(p[2],3)
        
        rotation_angle = math.radians(robot2_pose[2])
        x_transformed = x_translated*math.cos(rotation_angle) + y_translated*math.sin(rotation_angle)
        y_transformed = y_translated*math.cos(rotation_angle) - x_translated*math.sin(rotation_angle) 

        pt = [x_transformed, y_transformed, z_translated]
        if (z_translated>= 0.00):
            points_transformed.append(pt)
    
    fields = [PointField('x', 0, PointField.FLOAT32, 1), PointField('y', 4, PointField.FLOAT32, 1),PointField('z', 8, PointField.FLOAT32, 1)]

    header = Header()
    header.stamp = rospy.Time.now()
    header.frame_id = "world"
    pc2 = point_cloud2.create_cloud(header, fields, points_transformed)
    pub.publish(pc2)


# The default function 
def transform_points_robot(points_msg):
    #points_transformed = []

    for p in point_cloud2.read_points(points_msg, skip_nans=True):
        x_translated = round(p[0],3) + robot0_pose[0]
        y_translated = round(p[1],3) + robot0_pose[1]
        z_translated = round(p[2],3)
       
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


if __name__ == "__main__":
    points_transformed = []
    rospy.init_node('transform_cloud', anonymous=True)
    rospy.Subscriber('/octomap_point_cloud_centers', PointCloud2, transform_points_robot)
    #rospy.Subscriber('qbot1/octomap_point_cloud_centers', PointCloud2, transform_points_robot1)
    #rospy.Subscriber('qbot2/octomap_point_cloud_centers', PointCloud2, transform_points_robot2)
    rospy.sleep(0.5)
    rospy.spin()