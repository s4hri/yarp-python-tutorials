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
port = yarp.RpcClient()

# activate ports
port.open("/client")

top = 100
for i in range(1,top):
    # prepare a message to send
    bottle_in = yarp.Bottle()
    bottle_out = yarp.Bottle()
    bottle_out.addString("Hello")
    bottle_out.addInt32(i)
    print ("Sending ", bottle_out.toString())
    # send the message
    port.write(bottle_out, bottle_in)
    print ("Reply received: ", bottle_in.toString())
    yarp.delay(0.5)

# close the network
yarp.Network.fini()