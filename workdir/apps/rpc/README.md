# YARP RPC ports

## INTRODUCTION

In this repository is implemented a basic example of communication between RPC ports:
- a RPCClient (**/client**) that will send messages 
- a RPCServer (**/server**) that will receive the messages

To be able to communicate, the RPC ports have to be connected.
As communication protocols is used tcp.
Messages are sended through bottles objects.

The principal behavior of RPC ports is getting replies when a message is sended.

In the following image we can see an usual case of how message are sended/received/replied between ports with different rate.
![alt text][rpc]

#### RPCClient
When a **/client** is started, message are sended from this port, independently if there is some **/server** connected.
Once a **/client** is connected, the **/client** will wait to send a new message until receive the reply from **/server**.

#### RPCServer
When a **/server** is started, message are received from this port. If there is no message available, the **/server** port will wait until a new message is 
available.

To found more info about RPC ports and how they works have a look to [YARP - RPC ports](http://www.yarp.it/git-master/rpc_ports.html)

[rpc]:https://github.com/s4hri/yarp-python-tutorials/blob/master/workdir/media/rpc.png

## EXAMPLES: TEST YOURSELF

### RUN THE SCRIPTS
Be sure to be in the following path: 

  ```
  yarp-python-tutorial/workdir/apps/rpc
  ```
- **terminal 1**:  
               
      $~ python3 client.py
 
- **terminal 2**: 

      $~ python3 server.py

### WHAT HAPPENS IN THERE
#### terminal 1
The client.py script will:
- open a port called: **/client**
- send 100 "Hello i-th".
- print, if exists, the reply from the **/server** port

#### terminal 2
The server.py script will:
- open a port called: **/server**
- receive the message from the **/client** port and send a reply.

Notice that when the **/server** has received the message, the **/client** will wait until the **server** send back a reply.
