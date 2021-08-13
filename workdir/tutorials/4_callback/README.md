# YARP callback

## INTRODUCTION

In this repository is implemented a basic example of communication between buffered-ports using callback:
- a buffered-port (writer) that will send messages 
- a buffered-port (reader) that will receive the messages through callback

To be able to communicate, the buffered-ports have to be connected.
As communication protocols is used tcp.
Messages are sended through bottles, that in this case are attribute of buffered-ports.

The behavior of how callback works is highlighted when the ports work a different rate, expecally when the reader rate is greater thank writer rate.
They behave in an asynch mode.

In the following image we can see an usual case of how message are sended/readed between buffered-ports with different rate.
![alt text][bport]

#### buffered-port writer
When a writer buffered-port is started, message are sended from this port, independently if there is some reader port connected.
Also if a reader port is connected, the writer port will NOT wait to send a new message if the reader still has not terminated the read process.

#### buffered port read by callback
When a reader buffered-port by callback is started, message are received from this port. If there is no message available, the reader buffered-port by callback
will no wait for a new message. Instead, the process will go on with the same value from the last readed message. It will be automatically update when a new message
is received through the port.

To found more info about callback and how they works have a look to [YARP - buffered-ports](http://www.yarp.it/git-master/port_expert.html)

[bport]:https://github.com/s4hri/yarp-python-tutorials/blob/master/workdir/media/callback.png

## EXAMPLES: TEST YOURSELF
### RUN the script
Be sure to be in the following path inside the docker


      ~$ yarp-python-tutorial/tutorials/callback

Open a terminal and run:
  ```terminal
  ~$ bash run.sh
  ```

This command will open 2 terminal 

- **terminal 1**:

      ~$ python3 writer_bp.py
- **terminal 2**:

      ~$ python3 reader_bp_callback.py

### WHAT HAPPENS IN THERE
#### terminal 1
The writer_bp.py script will:
- open a buffered-port called: **/writer**
- send 100 "Hello i-th".

#### terminal 2
**N.B.** : the **terminal 2** will start with a delay respect to **terminal 1**.

The reader_bp_callback.py script will:
- open a buffered-port called: **/reader**
- create a connection between **/writer** and **/reader**
- continuously receiving updated message

Notice how the **/reader** has not loop inside the script, and then still receving update message from the **/writer**.
