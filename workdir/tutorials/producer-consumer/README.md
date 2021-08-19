# YARP producer-consumer

## INTRODUCTION

The producer-consumer problem is a classic example of multi-process synchronization problem. 
In a generic producer-consumer problem there are 3 parts:
1. prodcuer
2. consumer
3. buffer

In this repository is reproduced a producer-consumer problem with the
following features:
- rate_producer different from rate_consumer
- bounded buffer
- unbounded producer
- unbounded consumer
![alt_text][problem]


## YARP PROBLEM

Let's translate the basic example of producer-consumer by using yarp ports.

### PROBLEM SOLUTION

#### SOLUTION 1
A first solution coud be by using 3 different ports:
- a port (**/producer**) that will send items to the buffer
- a port (**/consumer**) that will receive the messages from the buffer 
- a port (**/buffer**) that will receive the messages from the producer and send the messages to the consumer
![alt_text][yarp_problem1]

With this approach we are not able to perform different rate for producer and consumer, since producer and consumer are connected to the same "buffer" port.

#### SOLUTION 2
To avoid this issue, we can add an additional port to the "buffer", so that producer and consumer can have a personal port and perform different rate. In total
there will be 4 different ports:
- a port (**/producer**) that will send items to the buffer
- a port (**/consumer**) that will receive the items from the buffer 
- a port (**/buffer_in**) that will receive the items from the producer
- a port (**/buffer_out**) that will send the items to the consumer

![alt_text][yarp_problem]

### PORT USAGE

We will continue this example using the **SOLUTION 2** with 4 ports.

#### /producer
When the **/producer** port is started, the **/producer** port will send items to the **/buffer_in** port.

If the buffer is full, **/producer** port will wait until the buffer is not full again.

#### /consumer
When a **/consumer** port is started, the **/consumer** port is ready to receive the items from the **/buffer_out** port.

If the buffer is empty, **/consumer** port will wait until the buffer is not empty again.

#### /buffer_in
When the **/buffer_in** port is started, the **/buffer_in** port is ready to receive the items from the **/producer** port.

If the buffer is full, **/buffer_in** port will append the read process until the buffer is not full again.


#### /buffer_out
When the **/buffer_out** port is started, the **/buffer_out** port is ready to send items to the **/consumer** port.

If the buffer is empty, **/buffer_out** port append the write process until the buffer is not empty again.


[problem]:https://github.com/s4hri/yarp-python-tutorials/blob/master/workdir/media/problem.png
[yarp_problem]:https://github.com/s4hri/yarp-python-tutorials/blob/master/workdir/media/yarp_problem.png
[yarp_problem1]:https://github.com/s4hri/yarp-python-tutorials/blob/master/workdir/media/yarp-problem1.png

## EXAMPLES: TEST YOURSELF

### RUN THE SCRIPTS
Be sure to be in the following path inside the docker:

    ~$ yarp-python-tutorial/tutorials/producer-consumer/


Open a terminal and run:
  ```terminal
  ~$ bash run.sh
  ```


This command will open 3 terminal (inside the container):
- **terminal 1**:

      ~$ python3 producer.py
- **terminal 2**:

      ~$ python3 consumer.py
- **terminal 3**:

      ~$ python3 buffer.py

### WHAT HAPPENS IN THERE
#### terminal 1
The producer.py script will:
- open a port called: **/producer**
- send n items to the **/buffer_in** port
- perfom tasks at random time (**rate_producer**)

#### terminal 2
The consumer.py script will:
- open a port called: **/consumer**
- receive items from the **/buffer_out** port
- perfom tasks at random time (**rate_consumer**)

#### terminal 3
The buffer.py script will:
- open a port called: **/buffer_in**
- open a port called: **/buffer_out**
- receive items through **/buffer_in** port from the **/producer** port
- send items from the **/buffer_out** port to **/consumer** port
- perform task with **rate_producer** and **rate_consumer**
