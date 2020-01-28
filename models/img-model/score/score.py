import json
import numpy as np
from tensorflow import keras
import os
import glob
#import dotenv
from azureml.core.model import Model
import base64
import io
from PIL import Image


MODEL_FILE_NAME = "img-model"

def init():
    global model
    model_path = Model.get_model_path(MODEL_FILE_NAME)
    #dotenv.load_dotenv()
    #model_path = os.getenv('AZUREML_MODEL_DIR')
    print("model_path: ", model_path)
    # deserialize the model file back into a sklearn model
    model = keras.models.load_model(model_path)
    print("Model Loaded")

def run(raw_data):
    try:
        data_dict = json.loads(raw_data)
        img_b64_decoded = base64.b64decode(data_dict['image'].encode("UTF-8"))
        buf = io.BytesIO(img_b64_decoded)
        img = Image.open(buf)
        imgs_as_np = np.array(img)
        #This line is probably not needed
        imgs_as_np = np.frombuffer(imgs_as_np, dtype=np.uint8).reshape(-1,28,28)
        print("image shape: ",imgs_as_np.shape)
        imgs_as_np = imgs_as_np/255.0
        proba = model.predict_proba(imgs_as_np)
        print("prediction: ",proba)
        result = {"predict_proba":proba.tolist()}
        return result
    except Exception as e:
        error = str(e)
        return error