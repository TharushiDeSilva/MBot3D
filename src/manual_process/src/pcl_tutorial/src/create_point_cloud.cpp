// this program creates a point cloud manually. 

#include "ros/ros.h"
#include "sensor_msgs/PointCloud2.h"
#include "sensor_msgs/point_cloud2_iterator.h"

ros::Publisher pub;
float point_data[] = {1.0, 1.0, 1.0, 2.0, 2.0, 2.0, 3.0, 3.0, 3.0, 4.0, 4.0, 4.0};
uint8_t color_data[] = {40, 80, 120, 160, 200, 240, 20, 40, 60, 80, 100, 120};

int main(int argc, char** argv){

    ros::init(argc, argv, "create_point_cloud"); 
    ros::NodeHandle nh; 
     
    sensor_msgs::PointCloud2 cloud_msg; 
    cloud_msg.header.frame_id = "map"; 
    cloud_msg.header.stamp = ros::Time::now();
    cloud_msg.height =1; 
    cloud_msg.width =4; 
    cloud_msg.is_bigendian = false;
    cloud_msg.is_dense = false;
    cloud_msg.point_step = 16; 
    cloud_msg.row_step = 16*4; 

    sensor_msgs::PointCloud2Modifier modifier(cloud_msg); 
    modifier.setPointCloud2Fields(4, 
                                    "x", 1, sensor_msgs::PointField::FLOAT32,
                                    "y", 1, sensor_msgs::PointField::FLOAT32,
                                    "z", 1, sensor_msgs::PointField::FLOAT32,
                                    "rgb", 1, sensor_msgs::PointField::FLOAT32);
    modifier.resize(100); 

    sensor_msgs::PointCloud2Iterator<float> iter_x(cloud_msg, "x");
    sensor_msgs::PointCloud2Iterator<float> iter_y(cloud_msg, "y");
    sensor_msgs::PointCloud2Iterator<float> iter_z(cloud_msg, "z");
    sensor_msgs::PointCloud2Iterator<uint8_t> iter_r(cloud_msg, "r");
    sensor_msgs::PointCloud2Iterator<uint8_t> iter_g(cloud_msg, "g");
    sensor_msgs::PointCloud2Iterator<uint8_t> iter_b(cloud_msg, "b");

    for(size_t i=0; i<4; ++i, ++iter_x, ++iter_y, ++iter_z, ++iter_r, ++iter_g, ++iter_b){
        *iter_x = point_data[3*i+0]; 
        *iter_y = point_data[3*i+1]; 
        *iter_z = point_data[3*i+2];
        *iter_r = color_data[3*i+0];
        *iter_g = color_data[3*i+1];
        *iter_b = color_data[3*i+2];
    }
    
    pub = nh.advertise<sensor_msgs::PointCloud2>("output_cloud",1000);
    pub.publish(cloud_msg);

    ros::spin();

}