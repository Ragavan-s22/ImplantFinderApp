# my_custom_layers.py
import tensorflow as tf
from tensorflow.keras.layers import Layer

# Example custom layer (if you have any)
class MyCustomLayer(Layer):
    def __init__(self, **kwargs):
        super(MyCustomLayer, self).__init__(**kwargs)

    def call(self, inputs):
        return tf.nn.relu(inputs)

# Register the custom layer
from tensorflow.keras.utils import get_custom_objects
get_custom_objects().update({"MyCustomLayer": MyCustomLayer})