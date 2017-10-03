#!/usr/bin/env python
# Created by Fuheng Deng on 08/29/2017

import rospy
import struct
import sys
from can_msgs.msg import Frame
from dataspeed_can_msgs.msg import *
from CanInterface import CanInterface
from canlib import *

class can2ros:
    def __init__(self, can_hardware_id=None, can_circuit_id=0):
        rospy.loginfo('starting caninterface...')
        try:
            self.canInterface = CanInterface(can_hardware_id, can_circuit_id)
            self.pub_can_rx = rospy.Publisher('/can_rx', CanMessageStamped, queue_size=1)
        except:
            rospy.logerr('can interface init failed...')
            sys.exit()
        self.start()

    def start(self):
        rospy.logdebug('Start publishing message...')
        while not rospy.is_shutdown():
            try:
                for i in range(85):
                    #Use canlib to read can data
                    frame = CanMessageStamped()
                    frame.msg = CanMessage()
                    frame.msg.id, msg, frame.msg.dlc, flg, time = self.canInterface.ch.read()
                    rospy.logdebug('hello world')
                    frame.header.stamp = rospy.Time.now()
                    is_error = (flg & canMSG_ERROR_FRAME > 0) # Error Frame Flag
                    frame.msg.extended = (flg & canMSG_EXT > 0) #Extended Frame Flag
                    if not is_error:
                        frame.msg.data = list(msg)
                        self.pub_can_rx.publish(frame)
            except (canNoMsg) as ex:
                pass
            except (canError) as ex:
                rospy.logerr("CAN Error: " + str(ex))
        rospy.spin()
        

if __name__ == "__main__":
    rospy.init_node('can2ros', anonymous=True)
    _ = can2ros(36847,0)
    rospy.spin()
