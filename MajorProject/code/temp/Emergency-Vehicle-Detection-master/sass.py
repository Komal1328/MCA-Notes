import tensorflow as tf

# Load the TensorFlow frozen model
model_path = 'C:/Users/ASUS/Desktop/Emergency-Vehicle-Detection-master/frozen_east_text_detection.pb'
with tf.io.gfile.GFile(model_path, 'rb') as f:
    graph_def = tf.compat.v1.GraphDef()
    graph_def.ParseFromString(f.read())
