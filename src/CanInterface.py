#!/usr/bin/env python
import sys
import canlib
import rospy

cl = canlib.canlib()

class CanInterface:

    def __init__(self, can_serial_number=0, can_circuit_id=0):
        self.channel = None
        self.ch = None
        
        #Get Channel from serial number and circuit id
        for i in range(cl.getNumberOfChannels()):
            if(can_serial_number == cl.getChannelData_Serial(i)):
                self.channel = i + can_circuit_id
                break

        if(self.channel == None):
            rospy.logerr("CAN Interface Error: Incorrect serial_number or can_circuit_id.")
            sys.exit()
        self.setUp(self.channel)

    def setUp(self, channel):
        channels = cl.getNumberOfChannels()
        if self.channel >= channels:
            rospy.loginfo('Invalid channel number')
            sys.exit()
        try:
            self.ch = cl.openChannel(self.channel, canlib.canOPEN_ACCEPT_VIRTUAL)
            self.ch.setBusOutputControl(canlib.canDRIVER_NORMAL)
            self.ch.setBusParams(canlib.canBITRATE_500K, 4, 3, 1, 1, 0)
            self.ch.busOn()
        except (canlib.canError) as ex:
            rospy.logerr("CAN Interface Error: " + str(ex))
            raise ex

            
