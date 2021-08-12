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

# define port and bottle
port = yarp.BufferedPortBottle()
bottle = port.prepare()

# activate ports
port.open("/subscriber3")

while True:
    # read messge
    bottle = port.read().toString()
    print("Received ", bottle)
    yarp.delay(5)

# deactivate ports
port.close()

# close the network
yarp.Network.fini()