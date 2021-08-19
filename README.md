# YARP Tutorials (Python)
![alt text][YARP-PY]

[YARP-PY]:https://github.com/s4hri/yarp-python-tutorials/blob/master/workdir/media/yarp-python-tutorial.png

This repository contains open source software to start programming in YARP using Python.

[YARP](http://www.yarp.it) is an open source library designed for implementing robotics applications.


# 1. Basic Tutorials
In the following you can find some tutorials for Python developers to start using YARP with:

- [Ports](https://github.com/s4hri/yarp-python-tutorials/tree/master/workdir/tutorials/ports)

- [Buffered Port](https://github.com/s4hri/yarp-python-tutorials/tree/master/workdir/tutorials/buffered-ports)

- [Rpc](https://github.com/s4hri/yarp-python-tutorials/tree/master/workdir/tutorials/rpc)

- [Callback](https://github.com/s4hri/yarp-python-tutorials/tree/master/workdir/tutorials/callbacks)



# 2. Common Patterns

In the following are implemented some example by using YARP for generical purpose, where communication are required
between different actors:

- [RFModule](https://github.com/s4hri/yarp-python-tutorials/tree/master/workdir/tutorials/rfmodule)

- [Producer-Consumer](https://github.com/s4hri/yarp-python-tutorials/tree/master/workdir/tutorials/producer-consumer)

- [Publisher-Subscriber](https://github.com/s4hri/yarp-python-tutorials/tree/master/workdir/tutorials/publisher-subscriber)


# 3. Performance
At the end, some benchmarks have been implemented to test the performance

- [Benchmarks](https://github.com/s4hri/yarp-python-tutorials/tree/master/workdir/tutorials/benchmarks)


# 4. How to run the tutorials (GNU/Linux)

- Requirements

  - make
  - Docker CE

- How to run the tutorials
The tutorials run inside a Docker container. To build and run the environment you can simply do:

    cd yarp-python-tutorials
    ./run.sh

A terminator process will be executed inside the Docker container just built. You can then, execute the tutorials browsing them in the file system.
For example to run the first tutorial you can type:

    cd ports
    bash run.sh
