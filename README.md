Works for ROS Kinetic 

How to install 

1. Clone the repository 
2. in the root: >> rosdep install -y --from-paths src --ignore-src --rosdistro kinetic 
3. catkin_make_isolated

How to Run 
1. the test node for a single robot 
	>> roslaunch multi_robot_exploration namespace_debug.launch
