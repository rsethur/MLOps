import json
import numpy as np
import pandas as pd
import joblib
from azureml.core.model import Model

MODEL_FILE_NAME = "risk-model"

def init():
    global model
    model_path = Model.get_model_path(MODEL_FILE_NAME)
    # deserialize the model file back into a sklearn model
    model = joblib.load(model_path)

def run(raw_data):
    try:
        data = json.loads(raw_data)['data']
        input_df = pd.DataFrame.from_dict(data)
        result = model.predict(input_df)
        return result.tolist()
    except Exception as e:
        error = str(e)
        return error