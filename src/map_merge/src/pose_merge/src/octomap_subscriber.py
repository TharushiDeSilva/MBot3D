#include "ros/ros.h"
#include "sensor_msgs/PointCloud2.h"

void octomap_centers_callback(const sensor_msgs::PointCloud2::ConstPtr& msg){
    ROS_INFO("Height is :[%d]", msg->height); 
    ROS_INFO("Width is: [%u]", msg->width);
}

int main(int argc, char **argv){
    ros::init(argc, argv, "octomap_centers"); 
    ros::NodeHandle nh; 
    ros::Subscriber sub = nh.subscribe("octomap_point_cloud_centers", 1000, point_cloud_callback);
    ros::spin();
    return 0;
}