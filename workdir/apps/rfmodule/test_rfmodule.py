#!/usr/bin/python3

# Copyright (C) 2006-2021 Istituto Italiano di Tecnologia (IIT)
# Copyright (C) 2006-2010 RobotCub Consortium
# All rights reserved.
#
# This software may be modified and distributed under the terms of the
# BSD-3-Clause license. See the accompanying LICENSE file for details.

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