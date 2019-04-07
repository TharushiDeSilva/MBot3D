Works for ROS Kinetic 

How to install 

1. Clone the repository 
2. in the root: >> rosdep install -y --from-paths src --ignore-src --rosdistro kinetic 
3. catkin_make_isolated

How to Run 

0. source the package as
    >> source devel_isolated/setup.bash
     
1. The greedy exploration full node for a single robot 
	>> roslaunch multi_robot_exploration greedy_exploration.launch 

2. Greedy exploration full node for a qbot0 in multi-robot system (change the name accordingly) 
    >> roslaunch multi_robot_exploration qbot0_greedy_exploration.launch 

3. Greedy exploration full node for a robot in a multi-robot system - with TF_prefix changes
    (change all the places where "qbot0" appears accordingly)

    >> roslaunch multi_robot_exploration test_tf_prefix.launch
-----------------------------------------------------------------------------------------------

To Test and debug, run the nodes separately in separate terminals. 

1. roslaunch kobuki_node minimal.launch 
2. roslaunch multi_robot_exploration tf_pub.launch 
3. roslaunch freenect_launch freenect.launch 
4. roslaunch octomap_server octomap_mapping.launch
5. roslaunch multi_robot_exploration my_navigation.launch
6. roslaunch explore_lite explore.launch 


