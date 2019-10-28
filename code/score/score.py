import json
import numpy as np
from sklearn.externals import joblib
from azureml.core.model import Model

MODEL_NAME = "creditcard-risk-model"

def init():
    global model
    model_path = Model.get_model_path(MODEL_NAME)
    # deserialize the model file back into a sklearn model
    model = joblib.load(model_path)

def run(raw_data):
    try:
        data = json.loads(raw_data)['data']
        data = np.array(data)
        result = model.predict(data)
        # you can return any datatype as long as it is JSON-serializable
        return result.tolist()
    except Exception as e:
        error = str(e)
        return error