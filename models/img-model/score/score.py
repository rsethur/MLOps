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
from inference_schema.parameter_types.standard_py_parameter_type import StandardPythonParameterType
from inference_schema.schema_decorators import input_schema, output_schema


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


input_sample = 'iVBORw0KGgoAAAANSUhEUgAAABwAAAAcCAAAAABXZoBIAAAA0klEQVR4nGNgGMyAWUhIqK5jvdSy/9/rUSTkVOJmrfoLAg/X/P102AFZzvDdXyj4HRsUZKGOolHoNljm2LbvH7HYFzAn++/fs9wM2rOwuYaPcdbfKNyO7f67jwmnJPe+v264tSp/fLgghxGXbOCHv3/LJXHJ6u76+3eaNC5Zgdg/f3fjtvjn358O2GX0mrb//Xseq4fUpzwFBuGvbVikJIrugoL3pB+mlLjTVXDIB2KaKbQaHCuHAzgxpMzXPAJJfWnlxmJbB1DmSnuLAHYfUB0AAPtta4Z9bfBAAAAAAElFTkSuQmCC'
output_sample = {"predict_proba":[[0.6428598165512085,7.802418622304685e-06,1.3926929568697233e-05,0.0009204870439134538,8.053903002291918e-06,0.35186225175857544,0.0001259837590623647,3.398631349682546e-07,2.572974381109816e-06,0.004198671784251928]]}

# Inference_schema generates a schema for your web service
# It then creates an OpenAPI (Swagger) specification for the web service
# at http://<scoring_base_url>/swagger.json
@input_schema('image', StandardPythonParameterType(input_sample))
@output_schema(StandardPythonParameterType(output_sample))
def run(image):
    try:
        img_b64_decoded = base64.b64decode(image.encode("UTF-8"))
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