import tensorflow as tf
import sys

PB_MODEL_PATH = sys.argv[-1]

converter = tf.lite.TFLiteConverter.from_saved_model(PB_MODEL_PATH)
converter.optimizations = [tf.lite.Optimize.DEFAULT]
tf_lite_model = converter.convert()
open('tflite_custom_model.tflite', 'wb').write(tf_lite_model)