# YARP benchmarks

## INTRODUCTION

In this repository is implemented a simpye test benchmarks to evaluate the difference performance between different
type of port and connection.

At this momemnt are tested:
- port
- rpc port
- rfmodule
with 2 different type of communication protocol:
- tcp
- fast_tcp

The test consist in send 100.000 sync message and wait for the reply. Each test is repeat for 10 time. 
Above are reported the result from this test (each plot is plotting the mean and std for each test).


![alt text][port]
![alt text][rpc]
![alt text][rfmodule]

[port]:https://github.com/s4hri/yarp-python-tutorials/blob/master/workdir/media/test_port_1.png
[rpc]:https://github.com/s4hri/yarp-python-tutorials/blob/master/workdir/media/test_rpc.png
[rfmodule]:https://github.com/s4hri/yarp-python-tutorials/blob/master/workdir/media/test_rf_module.png

## EXAMPLES: TEST YOURSELF

### RUN THE SCRIPTS
Be sure to be in the following path inside the docker: 

      ~$ yarp-python-tutorial/tutorials/benchmarks

In each sub-folder you will find a run.sh.


Open a terminal and run:
  ```terminal
  ~$ bash run.sh
  ```

This command will open 2 terminal 
      
- **terminal 1**:
      
      ~$ python3 test_rfmodule.py
- **terminal 2**:

      ~$ python3 test_client_rpc.py
