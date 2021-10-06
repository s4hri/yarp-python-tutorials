terminator -x yarpdev --device fakeFrameGrabber --name /grabber
terminator -x yarpview
sleep 1
yarp connect /grabber /yarpview/img:i
terminator -x python3 snap.py
