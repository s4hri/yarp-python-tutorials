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

yarp.Network.init()

# alternative callback classes depending on the underlying data type:
# - yarp.PropertyCallback
# - yarp.TypedReaderCallbackImage(Rgb|Rgba|Mono|Mono16|Int|Float|RgbFloat)
# - yarp.TypedReaderCallbackVector (yarp.DVector)
# - yarp.TypedReaderCallbackSound
class CustomCallback(yarp.BottleCallback):
    def __init__(self):
        super().__init__()
        # remove this constructor if no class members need to be initialized,
        # keep the above parent constructor invocation otherwise

    def onRead(self, bot, reader):
        print("Port %s received: %s" % (reader.getName(), bot.toString()))

# alternative buffered port classes depending on the underlying data type:
# - yarp.BufferedPortProperty
# - yarp.BufferedPortImage(Rgb|Rgba|Mono|Mono16|Int|Float|RgbFloat)
# - yarp.BufferedPortVector (yarp.DVector)
# - yarp.BufferedPortSound
p = yarp.BufferedPortBottle()
p.open("/reader")
c = CustomCallback()
p.useCallback(c)

print("Callback ready at port " + p.getName())
input("Press ENTER to quit\n")

p.interrupt()
p.close()

yarp.Network.fini()
