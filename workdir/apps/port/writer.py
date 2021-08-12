#!/usr/bin/python3

# Copyright (C) 2006-2021 Istituto Italiano di Tecnologia (IIT)
# Copyright (C) 2006-2010 RobotCub Consortium
# All rights reserved.
#
# This software may be modified and distributed under the terms of the
# BSD-3-Clause license. See the accompanying LICENSE file for details.

import yarp

# create the network
yarp.Network.init()

# define ports
outport = yarp.Port()
bottle = yarp.Bottle()

# activate ports
outport.open("/writer")

top = 100
for i in range(1,top):
    # prepare a message to send
    bottle.clear()
    bottle.addString("Hello")
    bottle.addInt32(i)
    print ("Sending ", bottle.toString())
    
    # send the message
    outport.write(bottle)
    yarp.delay(0.5)

# close the network
yarp.Network.fini()