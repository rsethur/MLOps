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

def run(input_df):
    try:
        #data = json.loads(raw_data)['data']
        #input_df = pd.DataFrame.from_dict(data)
        sno = input_df["Sno"]
        input_df = input_df.drop("Sno", axis=1).drop("Risk", axis=1)
        pred = model.predict(input_df)
        # convert to pandas series
        pred = pd.Series(pred, name="Risk")

        #create a dataframe to return
        result = pd.concat([sno, pred], axis=1)

        return result
    except Exception as e:
        error = str(e)
        return error