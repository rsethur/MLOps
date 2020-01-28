import numpy as np
import os
import base64
from models.img-model.batch_score import batch_score

DATASET_PATH = "models/img-model/dataset/data/"

img_path_list = []
for i in range(2):
    img_path = os.path.join(DATASET_PATH, str(i)+".png")
    img_path_list.append(img_path)

batch_score.init()

df = batch_score.run(img_path_list)
print(df)
