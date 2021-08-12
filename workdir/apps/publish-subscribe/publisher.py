#!/usr/bin/python3

# Copyright (C) 2006-2021 Istituto Italiano di Tecnologia (IIT)
# Copyright (C) 2006-2010 RobotCub Consortium
# All rights reserved.
#
# This software may be modified and distributed under the terms of the
# BSD-3-Clause license. See the accompanying LICENSE file for details.

import yarp
import random
from random import randint
import time

# create the network
yarp.Network.init()

# define port and bottle
port = yarp.BufferedPortBottle()
bottle = port.prepare()

# activate port
port.open("/publisher")

top = 1000
for i in range(1,top):
    bottle = port.prepare()
    bottle.clear()
    bottle.addInt32(i)
    # send the message
    port.write()
    print("sended: ", i)
    yarp.delay(0.5)    

# deactivate ports
port.close()

# close the network
yarp.Network.fini()