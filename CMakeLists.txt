cmake_minimum_required(VERSION 2.8.3)
project(ros2can_util)

## Compile as C++11, supported in ROS Kinetic and newer
# add_compile_options(-std=c++11)

## Find catkin macros and libraries
## if COMPONENTS list like find_package(catkin REQUIRED COMPONENTS xyz)
## is used, also find other catkin packages
find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  std_msgs
)

## Generate messages in the 'msg' folder
#add_message_files(
#    FILES
#)


## Generate added messages and services with any dependencies listed here
generate_messages(
   DEPENDENCIES
   std_msgs
)


#catkin_package(
#   INCLUDE_DIRS include
#   LIBRARIES ros2can
#   CATKIN_DEPENDS roscpp rospy std_msgs message_runtime
#   DEPENDS system_lib
# )
