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
outport = yarp.BufferedPortBottle()
# alternative buffered port classes depending on the underlying data type:
# - yarp.BufferedPortProperty
# - yarp.BufferedPortImage(Rgb|Rgba|Mono|Mono16|Int|Float|RgbFloat)
# - yarp.BufferedPortVector (yarp.DVector)
# - yarp.BufferedPortSound

# activate ports
outport.open("/writer")

top = 100
for i in range(1,top):
    # prepare a message to send
    bottle = outport.prepare()
    bottle.clear()
    bottle.addString("Hello")
    bottle.addInt32(i)
    print ("Sending ", bottle.toString())
    
    # send the message
    outport.write()
    yarp.delay(0.5)

# deactivate ports
outport.close()

# close the network
yarp.Network.fini()
