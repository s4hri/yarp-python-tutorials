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
port = yarp.RpcServer()

# activate ports
port.open("/server")

# place to store thing
bottle_in = yarp.Bottle()
bottle_out = yarp.Bottle()

top = 100
for i in range(1,top):
    port.read(bottle_in, True)
    print("Readed: ", bottle_in.toString())
    bottle_out.clear()
    msg = "Message " + bottle_in.toString() + " received in cycle: "
    bottle_out.addString(msg)
    bottle_out.addInt32(i)
    port.reply(bottle_out)
    yarp.delay(3)

# close the network
yarp.Network.fini()