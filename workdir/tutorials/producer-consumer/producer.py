"""
BSD 2-Clause License

Copyright (c) 2021, Nicola Severino Russi (nicola.russi@iit.it),
                    Davide De Tommaso (davide.detommaso@iit.it)
                    Social Cognition in Human-Robot Interaction
                    Istituto Italiano di Tecnologia, Genova
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this
   list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice,
   this list of conditions and the following disclaimer in the documentation
   and/or other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""

import yarp
import random
from random import randint
import time

# create the network
yarp.Network.init()

# define port and bottle
port = yarp.Port()
bottle = yarp.Bottle()

# activate port
port.open("/producer")

# define port name to connect
buffer = "/buffer_in"

# items to produce
itemsToProduce = ["apple", "orange", "pear", "banana", "kiwi", "watermelon", "peach", "grapes","strawberry"]

print("Producer writer started")
while itemsToProduce:
    # before writing check connection
    if yarp.Network.isConnected(port.getName(), buffer):
        # prepare the message
        bottle.clear()
        item = random.choice(itemsToProduce)
        itemsToProduce.remove(item)
        bottle.addString(item)
        # send message
        port.write(bottle)
        print ("sended ", bottle.toString())
    time.sleep(randint(1,2))

# deactivate ports
port.close()
print("Producer writer ended")

# close the network
yarp.Network.fini()
