#!/usr/bin/env python

from moveit_tutorial_tools import *


if __name__ == '__main__':
    
    init_node()
    
    group = MoveGroupCommander("manipulator")
    
    # Pose Target 1
    rospy.loginfo( "Start Pose Target 1")
    pose_target_1 = Pose()
    
    pose_target_1.position.x = 0.0
    pose_target_1.position.y = -0.6
    pose_target_1.position.z = 0.3
    pose_target_1.orientation.x = 1.0
    pose_target_1.orientation.y = 0.0
    pose_target_1.orientation.z = 0.0
    pose_target_1.orientation.w = 0.0
    
    rospy.loginfo( "Set Target to Pose:\n{}".format( pose_target_1 ) )
    group.set_pose_target( pose_target_1 )
    group.go()
    
    # Pose Target 2
    rospy.loginfo( "Start Pose Target 2")
    pose_target_2 = Pose()
    
    pose_target_2.position.x = 0.6
    pose_target_2.position.y = 0.0
    pose_target_2.position.z = 0.3
    pose_target_2.orientation.x = -0.707
    pose_target_2.orientation.y = -0.707
    
    rospy.loginfo( "Set Target to Pose:\n{}".format( pose_target_2 ) )
    group.set_pose_target( pose_target_2 )
    group.go()
    
    
