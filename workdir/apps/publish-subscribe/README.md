# YARP publisher-subscriber

## INTRODUCTION

In this repository is implemented a basic example of publisher-subscriber:
- a **publisher** (writer) will send messages at certain rate
- more **subscribers** (reader) can read the message at different rates

To be able to read from publisher, the subscribers have to be connected.
Buffered ports are used for this example.
Tcp is used as communication protocol.
Messages are sended through bottles, that in this case are attribute of buffered-ports.

Publisher-subsriber behave in an asynch mode.

In the following image we can see an example of publisher-subscirber, where each subscriber has a different rate.
![alt text][port]

#### Publisher
When a publisher is started, message are sended trhough buffered port, independently if there is some subscriber connected.

#### Subscriber
When a subscriber is started, message are readed from this port. If there is no message available, the subscriber will wait until a message is available.

[port]:https://github.com/s4hri/yarp-python-tutorials/blob/master/workdir/media/pub-sub.png

## EXAMPLES: TEST YOURSELF
### RUN the script
Be sure to be in the following path inside the docker.

    ~$ yarp-python-tutorial/workdir/apps/publish-subscribe
 

- **terminal 1**: 
      
      ~$ python3 publisher.py
- **terminal 2**: 
      
      ~$ python3 subscriber1.py
- **terminal 3**:

      ~$ python3 subscriber2.py
- **terminal 4**:

      ~$ python3 subscriber3.py

### WHAT HAPPENS IN THERE
#### terminal 1
The publisher.py script will:
- open a buffered-port called: **/publisher**
- send 1000 "sended: i-th" with rate: 0.5 s.

#### terminal 2
The subscriber1.py script will:
- open a buffered-port called: **/subscriber1**
- create a connection between **/publisher** and **/subscriber1**
- read the messages with rate: 1 s.

#### terminal 3
The subscriber1.py script will:
- open a buffered-port called: **/subscriber2**
- create a connection between **/publisher** and **/subscriber2**
- read the messages with rate: 3 s.

#### terminal 4
The subscriber1.py script will:
- open a buffered-port called: **/subscriber3**
- create a connection between **/publisher** and **/subscriber3**
- read the messages with rate: 5 s.

Notice how each **subscriber** read from the **publisher** at different rate.
