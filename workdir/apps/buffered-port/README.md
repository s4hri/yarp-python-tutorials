# YARP buffered-ports

## INTRODUCTION

In this repository is implemented a basic example of communication between buffered-ports:
- a buffered-port (writer) that will send messages 
- a buffered-port (reader) that will receive the messages

To be able to communicate, the buffered-ports have to be connected.
As communication protocols is used tcp.
Messages are sended through bottles, that in this case are attribute of buffered-ports.

The behavior of how buffered ports works is highlighted when the ports work a different rate. They behave in an asynch mode.

In the following image we can see an usual case of how message are sended/readed between buffered-ports with different rate.
![alt text][port]

#### buffered-port write
When a writer buffered-port is started, message are sended from this port, independently if there is some reader port connected.
Also if a reader port is connected, the writer port will NOT wait to send a new message if the reader still has not terminated the read process.

#### buffered port read
When a reader buffered-port is started, message are received from this port. If there is no message available, the reader buffered-port will wait until a message is available.

To found more info about buffered-ports and how they works have a look to [YARP - buffered-ports](https://www.yarp.it/latest/note_ports.html)

[port]:https://github.com/s4hri/yarp-python-tutorials/blob/master/media/buffered_port.png

## EXAMPLES: TEST YOURSELF
### RUN the script
Be sure to be in the following path: *yarp-python-tutorial/apps/buffered-port* and follow the command below

Open a terminal and run:

  ```terminal
  ~$ bash run.sh
  ```

This command will open 2 terminal (inside the container):
- **terminal 1**: run writer_bp.py
- **terminal 2**: run reader_bp.py

### WHAT HAPPENS IN THERE
#### terminal 1
The writer_bp.py script will:
- open a buffered-port called: **/writer**
- send 100 "Hello i-th".

#### terminal 2
**N.B.** : the **terminal 2** will start with a delay respect to **terminal 1**.

The reader_bp.py script will:
- open a buffered-port called: **/reader**
- create a connection between **/writer** and **/reader**
- receive only one message and then wait some time before ending the process.

Notice that when the **/reader** has received the message, the **/writer** will NOT wait to send a new message either the **readerd** has not terminated.
