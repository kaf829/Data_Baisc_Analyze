import tensorflow as tf
print("TensorFlow version:", tf.__version__)
print("GPU Devices:", tf.config.list_physical_devices('GPU'))


import sys
print(sys.executable)