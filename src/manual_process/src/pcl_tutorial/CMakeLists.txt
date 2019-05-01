cmake_minimum_required(VERSION 2.8.3)
project(pcl_tutorial)

# add_compile_options(-std=c++11)

find_package(catkin REQUIRED COMPONENTS
  pcl_conversions
  pcl_ros
  roscpp
  sensor_msgs
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

add_executable(octomap_subscriber src/octomap_subscriber.cpp)
target_link_libraries(octomap_subscriber ${catkin_LIBRARIES})
add_dependencies(octomap_subscriber pcl_tutorial_generate_messages_cpp)
