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
import sys

VOCAB_QUIT = yarp.createVocab("q", "u", "i", "t")

class Mymodule(yarp.RFModule):

    def __init__(self):
        yarp.RFModule.__init__(self)

        self.handlePort = yarp.Port()
        self.count = 0
        self.period = 0.0

    def getPeriod(self):
        return self.period

    def updateModule(self):
        self.count += 1
        print("%s updateModule" % self.count)
        return True

    def respond(self, command, reply):
        print("Responding to command")
        if command.check("period"):
            self.period = command.find("period").asFloat64()
            reply.addString("ack")
            return True
        elif command.get(0).asVocab() == VOCAB_QUIT:
            print("bye bye ...")
            reply.addString("bye")
            #yarp.RFModule.stopModule(False)
            return False
        #return yarp.RFModule.respond(command, reply)
        return True

    def configure(self, rf):
        self.count = 0
        self.period = 1.0
        self.handlePort.open("/myModule")
        self.attach(self.handlePort)
        if rf.check("period"):
            self.period = rf.find("period").asFloat64()
        return True

    def interruptModule(self):
        print("Interrupting your module, for port cleanup")
        return True

    def close(self):
        print("Calling close function")
        self.handlePort.close()
        return True


if __name__ == '__main__':

    yarp.Network.init()
    module = Mymodule()
    rf = yarp.ResourceFinder()
    rf.configure(sys.argv)
    print("Configure module...")
    module.configure(rf)
    print("Start module...")
    module.runModule()
    print("Main returning...")
