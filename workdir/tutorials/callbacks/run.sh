terminator -x python3 writer_bp.py 
terminator -x python3 reader_bp_callback.py 
sleep 1
yarp connect /writer /reader