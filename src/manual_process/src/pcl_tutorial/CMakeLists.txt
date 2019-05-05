cmake_minimum_required(VERSION 2.8.3)
project(pcl_tutorial)

# add_compile_options(-std=c++11)

find_package(catkin REQUIRED COMPONENTS
  pcl_conversions
  pcl_ros
  roscpp
  sensor_msgs
  geometry_msgs
)

catkin_package()

include_directories(
  ${catkin_INCLUDE_DIRS}
)

add_executable(talker src/talker.cpp)
target_link_libraries(talker ${catkin_LIBRARIES})
add_dependencies(talker pcl_tutorial_generate_messages_cpp)

add_executable(listener src/listener.cpp)
target_link_libraries(listener ${catkin_LIBRARIES})
add_dependencies(listener pcl_tutorial_generate_messages_cpp)

#add_executable(octomap_transformer src/octomap_transformer.cpp)
#target_link_libraries(octomap_transformer ${catkin_LIBRARIES})
#add_dependencies(octomap_transformer pcl_tutorial_generate_messages_cpp)

add_executable(example_point_cloud src/example_point_cloud.cpp)
target_link_libraries(example_point_cloud ${catkin_LIBRARIES})
add_dependencies(example_point_cloud pcl_tutorial_generate_messages_cpp)

add_executable(create_point_cloud src/create_point_cloud.cpp)
target_link_libraries(create_point_cloud ${catkin_LIBRARIES})
add_dependencies(create_point_cloud pcl_tutorial_generate_messages_cpp)