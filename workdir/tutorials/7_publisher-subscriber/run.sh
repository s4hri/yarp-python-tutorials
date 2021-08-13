terminator -x python3 publisher.py
terminator -x python3 subscriber1.py
terminator -x python3 subscriber2.py
terminator -x python3 subscriber3.py
sleep 1
yarp connect /publisher /subscriber1
yarp connect /publisher /subscriber2
yarp connect /publisher /subscriber3