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
import threading
from threading import Condition
from queue import Queue
import time


### ----------- DEFINE ------------ ###
## PORTS
# define ports and bottles of node
port_in = yarp.Port()
port_out = yarp.Port()
bottle_in = yarp.Bottle()
bottle_out = yarp.Bottle()

# define port name
producer= "/producer"
consumer = "/consumer"


## CLASSE BUFFER
# define a queue with conditions
class Buffer:
    def __init__(self, size):
        self.Common = Queue(size)
        self.EmptyCondition = Condition()
        self.FullCondition = Condition()


## PROCESSES
# buffer read from producer:
def buffer_reader(q, port, bottle, prod):
    print("Buffer reader started")
    while True:
        # read messge
        port.read(bottle)
        # exit condition
        if q.Common.empty() and not yarp.Network.exists(prod):
            break
        # waiting condition
        elif q.Common.full():
            with q.FullCondition:
                print("buffer full, waiting consumer")
                q.FullCondition.wait()
                q.Common.put(bottle.toString())
                print("added ", bottle.toString(), " in buffer: ", list(q.Common.queue))
        # normal condition
        else:
            with q.EmptyCondition:
                q.Common.put(bottle.toString())
                q.EmptyCondition.notify()
                print("added ", bottle.toString(), " in buffer: ", list(q.Common.queue))
    port.close()
    print("Buffer reader ended")

# buffer write to consumer
def buffer_writer(q, port, bottle, prod, cons):
    exitFlag = False
    print("Buffer writer started")
    while not exitFlag:
        # before writing check connection
        if yarp.Network.isConnected(port.getName(), cons):
            if q.Common.empty():
                # exit condition
                if not yarp.Network.exists(prod):
                    exitFlag = True
                    break
                # waiting condition
                else:
                    with q.EmptyCondition:
                        print("buffer empty, waiting producer")
                        q.EmptyCondition.wait()
            # normal condition
            else:
                with q.FullCondition:
                    # prepare the message
                    bottle.clear()
                    item = q.Common.get()
                    bottle.addString(item)
                    # send the message
                    port.write(bottle)
                    q.FullCondition.notify()
                    print("taken ", bottle.toString(), " from buffer: ", list(q.Common.queue))
    port.close()
    print("Buffer writer ended")


### ----------- MAIN ------------ ###

# initialize queue
queue = Buffer(3)

# create the network
yarp.Network.init()

# active ports
port_in.open("/buffer_in")
port_out.open("/buffer_out")

# initialize process
br = threading.Timer(0, buffer_reader, [queue, port_in, bottle_in, producer])
bw = threading.Timer(0, buffer_writer, [queue, port_out, bottle_out, producer, consumer])

# start process
br.start()
bw.start()

# waiting end process
br.join()
bw.join()

# close the network
yarp.Network.fini()
