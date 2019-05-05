// this is an example program to subscrie to an existing point colud and assign it to another topic and republish. 
// A trail code. does not contribute to the program.

#include <ros/ros.h>
#include <sensor_msgs/PointCloud2.h>
#include <pcl-1.8/pcl/conversions.h>
#include <pcl_conversions/pcl_conversions.h>
#include <pcl-1.8/pcl/point_cloud.h>
#include <pcl-1.8/pcl/point_types.h> 

ros::Publisher pub; 

void cloud_callback(const sensor_msgs::PointCloud2ConstPtr&

 input){
    //create container for the data
    sensor_msgs::PointCloud2 output; 
    //do the processing 
    output = *input; 
    //publish the data 
    pub.publish(output); 
}

int main(int argc, char** argv){
    //Initialize ros node
    ros::init(argc, argv, "pcl_publish_subscribe_example"); 
    ros::NodeHandle nh; 

    //create a ros subscriber for the input point cloud
    ros::Subscriber sub = nh.subscribe("octomap_point_cloud_centers", 1, cloud_callback); 

    //Create a ROS publisher for the output point cloud
    pub = nh.advertise<sensor_msgs::PointCloud2>("output_cloud",1);

    //spin
    ros::spin();
}