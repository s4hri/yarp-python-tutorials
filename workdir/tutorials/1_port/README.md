# YARP ports

## INTRODUCTION

In this repository is implemented a basic example of communication between ports:
- a port (writer) that will send messages 
- a port (reader) that will receive the messages

To be able to communicate, the ports have to be connected.
As communication protocols is used tcp.
Messages are sended through bottles objects.

The behavior of how ports works is highlighted when the ports work a different rate.

In the following image we can see an usual case of how message are sended/readed between ports with different rate.
![alt text][port]

#### port write
When a writer port is started, message are sended from this port, independently if there is some reader port connected.
Once a reader port is connected, the writer port will wait to send a new message until the reader has terminate the read process.

#### port read
When a reader port is started, message are received from this port. If there is no message available, the reader port will wait until a message is available.

To found more info about ports and how they works have a look to [YARP - ports](https://www.yarp.it/latest/note_ports.html)

[port]:https://github.com/s4hri/yarp-python-tutorials/blob/master/workdir/media/port.png

## EXAMPLES: TEST YOURSELF

### RUN THE SCRIPTS
Be sure to be in the following path inside the docker:

      ~$ yarp-python-tutorial/workdir/apps/port


- **terminal 1**:
  
      ~$ python3 writer.py
- **terminal 2**:

      ~$ python3 reader.py

### WHAT HAPPENS IN THERE
#### terminal 1
The writer.py script will:
- open a port called: **/writer**
- send 100 "Hello i-th".

#### terminal 2
**N.B. **: the **terminal 2** will start with a delay respect to **terminal 1**.

The reader.py script will:
- open a port called: **/reader**
- create a connection between **/writer** and **/reader**
- receive only one message and then wait some time before ending the process.

Notice that when the **/reader** has received the message, the **/writer** will wait until the **readerd** has terminated to send a new message.
