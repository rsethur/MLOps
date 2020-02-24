import json
import numpy as np
import pandas as pd
import joblib
from azureml.core.model import Model
from inference_schema.parameter_types.standard_py_parameter_type import StandardPythonParameterType
from inference_schema.schema_decorators import input_schema, output_schema

MODEL_FILE_NAME = "risk-model"

def init():
    global model
    model_path = Model.get_model_path(MODEL_FILE_NAME)
    # deserialize the model file back into a sklearn model
    model = joblib.load(model_path)


input_sample = {'Age':[20],'Sex':['male'],'Job':[0],'Housing':['own'],'Savingaccounts':['little'],'Checkingaccount':['little'],'Creditamount':[100],'Duration':[48],'Purpose':['radio/TV']}
output_sample = {'predict_proba':[[0.6900664207902254,0.30993357920977466]]}

# Inference_schema generates a schema for your web service
# It then creates an OpenAPI (Swagger) specification for the web service
# at http://<scoring_base_url>/swagger.json
@input_schema('data', StandardPythonParameterType(input_sample))
@output_schema(StandardPythonParameterType(output_sample))
def run(data):
    try:
        input_df = pd.DataFrame.from_dict(data)
        proba = model.predict_proba(input_df)
        result = {"predict_proba":proba.tolist()}
        return result
    except Exception as e:
        error = str(e)
        return error