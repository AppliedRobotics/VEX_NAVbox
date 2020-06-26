#!/usr/bin/env python
 
import rospy
import tf
from math import cos, sin, pi
from sensor_msgs.msg import JointState
from std_msgs.msg import String
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Point, Pose, Quaternion, Twist, Vector3

odom_broadcaster = tf.TransformBroadcaster()
def odom_cb(data):
	trans = (data.pose.pose.position.x, data.pose.pose.position.y, data.pose.pose.position.z)
	rot = (data.pose.pose.orientation.x,data.pose.pose.orientation.y,data.pose.pose.orientation.z,data.pose.pose.orientation.w)
	t = rospy.Time.now()
	odom_broadcaster.sendTransform(trans, rot, t, "base_footprint", "odom")
	

rospy.init_node('tf_broad', anonymous=True)
rate =rospy.Rate(5)
tf_broadcaster = tf.TransformBroadcaster()
rospy.Subscriber("odom", Odometry, odom_cb)
while not rospy.is_shutdown():
	time = rospy.Time.now()
	laser_quat = tf.transformations.quaternion_from_euler(0,0,pi)
	tf_broadcaster.sendTransform((0.1,0,0.1), laser_quat, time, "laser", "base_footprint")
	camera_quat = tf.transformations.quaternion_from_euler(0,pi/2,0)
	tf_broadcaster.sendTransform((0,0,0.16), camera_quat, time, "camera_rgb_optical_frame", "base_footprint") 
    # map_quat = tf.transformations.quaternion_from_euler(0,0,0)
    # odom_broadcaster.sendTransform((0,0,0), map_quat, time, "odom", "map")
	rate.sleep()
