import numpy
import yarp
import matplotlib.pyplot as plt

yarp.Network.init()


input_port = yarp.Port()
input_port.open("/snap")
yarp.Network.connect("/grabber", "/snap")

img_array = numpy.zeros((240, 320, 3), dtype=numpy.uint8)
yarp_image = yarp.ImageRgb()
yarp_image.resize(320, 240)
yarp_image.setExternal(img_array, img_array.shape[1], img_array.shape[0])

input_port.read(yarp_image)
plt.imshow(img_array)
plt.show()

input_port.close()
