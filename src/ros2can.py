#!/usr/bin/env python
# Created by Fuheng Deng on 08/29/2017

import rospy
import struct
import sys
from ros2can_util.msg import *
from CanInterface import CanInterface

class ros2can:
	def __init__(self, can_hardware_id=None, can_circuit_id=0):
		rospy.loginfo('starting caninterface...')
		try:
			self.canInterface = CanInterface(can_hardware_id, can_circuit_id)
			rospy.Subscriber('/can_tx', CanMessage, self.do_when_recv)
		except:
			rospy.logerr('can interface init failed...')
			sys.exit()

	def do_when_recv(self, data):
		rospy.logdebug(data.id)
		rospy.logdebug(data.data)
		self.canInterface.ch.write(data.id, data.data) # not sent yet
		self.canInterface.ch.ioCtl_flush_rx_buffer() # flush the buffer
		rospy.logdebug('sent!')

if __name__ == "__main__":
	rospy.init_node('ros2can', anonymous=True)
	_ = ros2can(0,0)
	rospy.spin()