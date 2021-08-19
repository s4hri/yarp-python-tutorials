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
import time
import numpy as np
import matplotlib.pyplot as plt

# create the network
yarp.Network.init()

# define ports
port = yarp.RpcClient()

# activate ports
port.open("/client")

# place to store thing
bottle_in  = yarp.Bottle()
bottle_out = yarp.Bottle()


# define
kind =  2   # tcp / fast_tcp
sets = 10   # how many reps
item =  2   # mean & std
reps = 100000   # repetitions


means = np.zeros((kind, sets))
stds  = np.zeros((kind, sets))

delta_t = np.zeros(reps)


for k in range(kind):
    # choose carrier
    if k == 0:
        yarp.Network.connect(port.getName(), '/myModule', 'tcp')
    else:
        yarp.Network.connect(port.getName(), '/myModule', 'fast_tcp')
    # start test
    for j in range(sets):
        for i in range(reps):
            bottle_out.clear()
            # prepare a message to send
            bottle_out.addString("test")
            bottle_out.addFloat32(i)
            # send the message
            print ("Sending ", bottle_out.toString())
            t0 = time.perf_counter()    # time msg sended
            port.write(bottle_out, bottle_in)
            # reply received
            print ("Reply received: ", bottle_in.toString())
            ti = time.perf_counter()    # time reply
            delta_t[i] = (ti - t0) * 1000.0
        # statistics
        means[k][j] = np.mean(delta_t)
        stds [k][j] = np.std (delta_t)
    # disconnect for the new connection
    yarp.Network.disconnect(port.getName(), '/myModule')

# plot
plt.figure()
plt.title("rpc client with rf_module")
plt.ylabel("time (ms)")
plt.xlabel("sets")
plt.grid(axis='y')
plt.errorbar(np.arange(sets), means[0], yerr=stds[0], fmt='-o', label='tcp')
plt.errorbar(0.2 + np.arange(sets), means[1], yerr=stds[1], fmt='-o', label='fast_tcp')
plt.legend()
plt.show()

# close the network
yarp.Network.fini()
