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
inport = yarp.BufferedPortBottle()

# activate ports
inport.open("/reader")

# create connection betweeen ports inside the network:
# note: connect(writer, reader)  ok
#       connect(reader, writer)  not ok
yarp.Network.connect("/writer", inport.getName())
    
# read the messge
bottle = inport.read().toString()
print("Received ", bottle)
yarp.delay(5)

# deactivate ports
inport.close()

# close the network
yarp.Network.fini()