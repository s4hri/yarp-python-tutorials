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
        yarp.Network.connect(port.getName(), '/server', 'tcp')
    else:
        yarp.Network.connect(port.getName(), '/server', 'fast_tcp')
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
plt.title("rpc")
plt.ylabel("time (ms)")
plt.xlabel("sets")
plt.grid(axis='y')
plt.errorbar(np.arange(sets), means[0], yerr=stds[0], fmt='-o', label='tcp')
plt.errorbar(0.2 + np.arange(sets), means[1], yerr=stds[1], fmt='-o', label='fast_tcp')
plt.legend()
plt.show()

# close the network
yarp.Network.fini()