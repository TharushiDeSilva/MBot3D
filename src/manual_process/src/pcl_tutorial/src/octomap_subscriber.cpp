// This program subscribe to octomap center points and get information. 

#include "ros/ros.h"
#include "sensor_msgs/PointCloud2.h"



void octomap_centers_cb(const sensor_msgs::PointCloud2::ConstPtr& msg){
    ROS_INFO("Height is :[%u]", msg->height); 
    ROS_INFO("Width is: [%u]", msg->width);
}

int main(int argc, char **argv){
    ros::init(argc, argv, "octomap_centers_sub"); 
    ros::NodeHandle nh; 
    ros::Subscriber sub = nh.subscribe("octomap_point_cloud_centers", 1000,
                                        octomap_centers_cb);
    ros::spin();
    return 0;
}