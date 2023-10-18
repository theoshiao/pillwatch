from roboflow import Roboflow
from config import *
from flask import Flask, request, jsonify
import tempfile
import os

TEST_IMAGE_PATH = "./images/test_image.jpg"
RF_PROJECT_NAME = "pills-sxdht" # https://universe.roboflow.com/roboflow-100/pills-sxdht/model/1

''' Given the file path for the image to identify, use model from roboflow to make a prediction '''
def predict_pill_from_image_path(image_path=TEST_IMAGE_PATH):
    # Retrieve pill identification model
    rf = Roboflow(api_key=ROBOFLOW_API_KEY_PRIVATE)
    project = rf.workspace().project(RF_PROJECT_NAME)
    model = project.version(1).model

    prediction = model.predict(image_path, confidence=30, overlap=30)
    return prediction.json()
    
