# YARP RFModule

## INTRODUCTION

In this repository is implemented a basic example of RFModule.

To be able to communicate with a RFModule you can use a RPC Client port.
As communication protocols is used tcp.

The RFModule help you to wrtie a generic module.

In the following image we can see a generic RFModule: it comes with pre-determinate function class, which are editable 
in the case we need some specific beahavior. Basically it will need at least one port (RPCServer or Port, in this example
called "myModule") to be able to
receive command. In addiction, with a RPC (Client) port it is possible to send command to the RFModule.
In this case the RPC (Client) port works as an interface to control the RFModule.

![alt text][rpc]

#### RFModule
When a **RFModule** is started, a RPCServer Port (or simple Port) is open ready to receive some command. If the RFModule 
receive a message from the RPC Client, the RFModule will send a reply to RPC Client.
Meanwhile, the RFModule it will start its configuration and functionality. The RFModule will be update at certain period/rate (also this parameter
could be editable).

#### RPC Client
When a **RPC Client** is started, message are sended from this port to the **RFModule**. Once a message it sended, RPC Client
will wait for the answer from the RFModule.

To found more info about RFModule and how they works have a look to [YARP - RFModule](http://www.yarp.it/git-master/yarp_rfmodule_tutorial.html)

[rpc]:https://github.com/s4hri/yarp-python-tutorials/blob/master/media/rfmodule.png

## EXAMPLES: TEST YOURSELF

### RUN THE SCRIPTS
Be sure to be in the following path: 
  ```terminal
  yarp-python-tutorial/apps/rfmodule
  ```
and follow the command below.

Open a terminal and run:
  ```terminal
  ~$ bash run.sh
  ```

This command will open 2 terminal (inside the container):
- **terminal 1**: run test_rfmodule.py
- **terminal 2**: run "yarp rpc /myModule" (**RPC Client port**)

### WHAT HAPPENS IN THERE
#### terminal 1
The test_rfmodule.py script will:
- open a port called: **/myModule**
- start the module (init, configure, ...)
- update the module (each period, editable)
- handle the command received
- handle the endign of the module (closing, stopping, ..)

#### terminal 2
The RPC Client port will:
- enable you to send message (in this case command) to the RFModule
