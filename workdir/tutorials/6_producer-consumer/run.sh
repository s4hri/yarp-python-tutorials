terminator -x python3 buffer.py
terminator -x python3 producer.py
terminator -x python3 consumer.py
sleep 1
yarp connect /producer /buffer_in
yarp connect /buffer_out /consumer