source /opt/ros/humble/setup.sh
source ~/turtlebot4_ws/install/setup.sh
export RMW_IMPLEMENTATION=rmw_fastrtps_cpp
[ -t 0 ] && export ROS_SUPER_CLIENT=True || export ROS_SUPER_CLIENT=False
export ROS_DOMAIN_ID=2
export ROS_DISCOVERY_SERVER=10.5.112.168:11811