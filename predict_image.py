from roboflow import Roboflow
from config import *

rf = Roboflow(api_key=ROBOFLOW_API_KEY_PRIVATE)
project = rf.workspace().project("pills-sxdht")

print(project)
model = project.version(1).model 

prediction = model.predict("./test_image.jpg", confidence=30, overlap=30)

print(prediction.json())
