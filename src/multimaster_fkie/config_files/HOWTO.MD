This directory is for files related to ROS_MASTER  configurations. 
Before running the package, make sure to change/add relevant host names into /etc/hosts file 

How to edit /etc/hosts file -----------
1. sudo <editor name> /etc/hosts
2. add/change the following section 
----------------------------------------------------------
# ROS multi-master connection details 
192.168.49.140	tharushi-X550LD     # IP of this robot  
192.168.49.8	qbot1-desktop       # IP's of other robots in the network
192.168.49.71	qbot2-destkop
----------------------------------------------------------
make sure they're all in the same IP domain, or networked properly.


After configuring the robots in the network, select a master for the process. 
source the master configuration file. 

>> source ~/MBot3D/multimaster_fkie/config_files/master_config.bash 

edit the relevant file before using. (select the master and change everyone's file accordingly) 