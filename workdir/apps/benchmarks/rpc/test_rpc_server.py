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
import time

# create the network
yarp.Network.init()

# define ports
port = yarp.RpcServer()

# activate ports
port.open("/server")

# place to store thing
bottle_in = yarp.Bottle()
bottle_out = yarp.Bottle()

while True:
    # read the message
    port.read(bottle_in, True)
    print("Readed: ", bottle_in.toString())
    bottle_out.clear()
    bottle_out.addString("received")
    # respond to the message
    port.reply(bottle_out)
# close the network
yarp.Network.fini()