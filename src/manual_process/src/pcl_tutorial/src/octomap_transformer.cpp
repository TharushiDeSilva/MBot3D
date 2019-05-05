// This program subscribe to octomap center points and get information. 

#include "ros/ros.h"
#include "sensor_msgs/PointCloud2.h"
#include "sensor_msgs/point_cloud2_iterator.h"
#include "pcl-1.8/pcl/conversions.h"
#include "pcl_ros/point_cloud.h"
#include "pcl_ros/transforms.h"
#include "pcl_conversions/pcl_conversions.h"
#include "eigen3/Eigen/Eigen"
#include "eigen3/Eigen/Geometry"
#include "tf2_sensor_msgs/tf2_sensor_msgs.h"
#include "geometry_msgs/TransformStamped.h"


using namespace std; 
using namespace tf2;
//using namespace Eigen;  
//using Eigen::Matrix4f; 

//static Eigen::Matrix4f transform_mat;
static bool initialized = false;   
ros::Publisher pub; 
const static geometry_msgs::TransformStamped pc_transformation;  

/*
void create_eigen_transform(){
    initialized = true; 
    transform_mat << 1.0, 0.0, 0.0, 0.0,
                    0.0, 1.0, 0.0, 0.0,
                    0.0, 0.0, 1.0, 0.0,
                    0.0, 0.0, 0.0, 1.0; 
}
*/
void set_transforms(){
    
    pc_transformation.header.frame_id = "map";
    pc_transformation.child_frame_id = "world"; 
    pc_transformation.transform.translation.x = 1.0;    //linear translation in x direction 
    pc_transformation.transform.translation.y = 0;      //linear translation in y direction 
    pc_transformation.transform.translation.z = 0;      //linear translation in z direction 
    pc_transformation.transform.rotation.x = 0;         //roll
    pc_transformation.transform.rotation.y = 0;         //pitch
    pc_transformation.transform.rotation.z = 0;         //yaw: only effective rotation for wheeled robots in even surface 
    pc_transformation.transform.rotation.w = 0;         
    initialized = true;     //assigning values once is enough. except for the timestamp. 
}

void octomap_centers_cb(const sensor_msgs::PointCloud2Ptr& points_msg){
   // ROS_INFO("Height is :[%u]", input_pc->height); 
    
    //sensor_msgs::PointCloud output_pc; 
    
    // pcl_ros::transformPointCloud(&transform_mat, &input_pc, &output_pc);
     
    //Following line works fine. just a test. 
    // cout<<"transform matrix is: "<< transform_mat<<endl;
    //pub.publish(output_pc);  

    /*
    int num_of_points = points_msg->width * points_msg->height;   //height is usually zero
    int point_length = points_msg->point_step; 
    int offset_x = points_msg->fields[0].offset;            //convensionally 0
    int offset_y = points_msg->fields[1].offset;            //conventionally 4 
    int offset_z = points_msg->fields[2].offset;            //conventionally 8
    */
    const sensor_msgs::PointCloud2 input_pc = *points_msg; 
    sensor_msgs::PointCloud2 output_pc; 
 
    
    //ROS_INFO("number of points : [%d]", points_msg->width * points_msg->height);
    //ROS_INFO("x offset: [%d], y offset: [%d], z offset: [%d]", offset_x, offset_y, offset_z);
    
    //since height is 1, we don't have to consider row_step parameter
   /* for(int i=0; i<num_of_points; i++){
        int position_of_x = i*point_length + offset_x; 
        int position_of_y = i*point_length + offset_y; 
        int position_of_z = i*point_length + offset_z; 

        ROS_INFO("count: [%d] \tX: [%d], \ty: [%d], \tz: [%d]", i, points_msg->data[position_of_x], points_msg->data[position_of_y], points_msg->data[position_of_z]);
    }*/
    /*
    sensor_msgs::PointCloud2Iterator<float> iter_x(*points_msg, "x"); 
    sensor_msgs::PointCloud2Iterator<float> iter_y(*points_msg, "y"); 
    sensor_msgs::PointCloud2Iterator<float> iter_z(*points_msg, "z"); 
    float x; float y; float z; 
    for(; iter_x != iter_x.end(); ++iter_x, ++iter_y, ++iter_z){
        *iter_x = x; 
        *iter_y = y; 
        *iter_z = z; 
        ROS_INFO("x: [%d]\ty: [%d]\tz: [%d]", x,y,z); 
    }
    */
    
   tf2::doTransform(input_pc, output_pc, pc_transformation);
   
   pub.publish(output_pc);
}


int main(int argc, char **argv){
    if(!initialized){
        set_transforms(); 
    }
    
    ros::init(argc, argv, "octomap_centers_transform"); 
    ros::NodeHandle nh; 
    ros::Subscriber sub = nh.subscribe("octomap_point_cloud_centers", 1, octomap_centers_cb);
    //Create a ROS publisher for the output point cloud
    pub = nh.advertise<sensor_msgs::PointCloud2>("output_cloud",1);
    ros::spin();
    return 0;
}