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
import sys

VOCAB_QUIT = yarp.createVocab("q", "u", "i", "t")

class Mymodule(yarp.RFModule):

    def __init__(self):
        yarp.RFModule.__init__(self)

        self.handlePort = yarp.Port()
        self.count = 0
        self.period = 0.0
        self.test = 0

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
        elif command.check("test"):
            self.test = command.get(1).asFloat32()
            reply.addString("received")
            reply.addFloat32(self.test)
            return True
        elif command.get(0).asVocab() == VOCAB_QUIT:
            print("bye bye ...")
            reply.addString("bye")
            return False
        return True
    
    def configure(self, rf):
        self.count = 0
        self.period = 0.000000001
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