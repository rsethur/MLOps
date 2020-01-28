import json
import numpy as np
import os
import base64
from models.img-model.score import score
from PIL import Image

DATASET_PATH = "models/img-model/dataset/data/"

#load data into numpy array
img_path = os.path.join(DATASET_PATH, "0.png")
with open(img_path, 'rb') as img_file:
    img_b64 = base64.b64encode(img_file.read()).decode("UTF-8")
input_dict = {"image":img_b64}

#init & score
score.init()

score.run(json.dumps(input_dict))


