import os
os.environ['TF_KERAS'] = '1'

from tensorflow.python.keras import backend as K
from tensorflow.python.keras.models import load_model
import onnx
import keras2onnx
from layers import BilinearUpSampling2D

onnx_model_name = 'nyu.onnx'

# Custom object needed for inference and training
custom_objects = {'BilinearUpSampling2D': BilinearUpSampling2D, 'depth_loss_function': None}

model = load_model('nyu.h5', custom_objects=custom_objects, compile=False)
onnx_model = keras2onnx.convert_keras(model, model.name)
onnx.save_model(onnx_model, onnx_model_name)