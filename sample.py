import tensorflow as tf

# Check available devices
gpus = tf.config.list_physical_devices('GPU')
if gpus:
    print("GPU is available:", gpus)
else:
    print("GPU is not available to TensorFlow.")
