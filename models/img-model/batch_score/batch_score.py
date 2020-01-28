import numpy as np
from tensorflow import keras
import dotenv
from azureml.core.model import Model
from PIL import Image
import pandas as pd
import tensorflow as tf

MODEL_FILE_NAME = "img-model"

def init():
    global model
    print("GPU USAGE: ", tf.test.is_gpu_available())
    model_path = Model.get_model_path(MODEL_FILE_NAME)
    dotenv.load_dotenv()
    print("model_path: ", model_path)
    # deserialize the model file back into a sklearn model
    model = keras.models.load_model(model_path)
    print("Model Loaded")

def run(file_list):
    try:
        df = pd.DataFrame(columns=["filename", "prediction"])
        for file_name in file_list:
            img = Image.open(file_name)
            img_as_np = np.array(img)
            img_as_np = np.expand_dims(img_as_np, axis=0)
            img_as_np = img_as_np / 255.0
            proba = model.predict_proba(img_as_np)
            pred = np.argmax(proba)
            print("prediction: ", pred)
            df = df.append(({"filename":file_name, "prediction":pred}), ignore_index=True)
        return df
    except Exception as e:
        error = str(e)
        return error