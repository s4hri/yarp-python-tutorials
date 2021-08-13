terminator -x python3 /home/docky/workdir/tutorials/1_producer-consumer/buffer.py &
terminator -x python3 /home/docky/workdir/tutorials/1_producer-consumer/producer.py &
terminator -x python3 /home/docky/workdir/tutorials/1_producer-consumer/consumer.py &
sleep 1
yarp connect /producer /buffer_in &
yarp connect /buffer_out /consumer
