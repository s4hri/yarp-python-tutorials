"""
MIT License

Copyright (c) 2021, Nicola Severino Russi (nicola.russi@iit.it),
                    Social Cognition in Human-Robot Interaction
                    Istituto Italiano di Tecnologia, Genova
All rights reserved.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
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