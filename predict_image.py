from roboflow import Roboflow
from config import *
from flask import Flask, request, jsonify
import tempfile
import os

TEST_IMAGE_PATH = "./images/test_image.jpg"
RF_PROJECT_NAME = "pills-sxdht" # https://universe.roboflow.com/roboflow-100/pills-sxdht/model/1
SQLALCHEMY_DATABASE_URI = 'pillwatch'

app = Flask(__name__)

app.config[SQLALCHEMY_DATABASE_URI] = f'postgresql://amyxjhuang:{POSTGRESQL_PASSWORD}@localhost/pillwatch'
db = SQLAlchemy(app)


''' Given the file path for the image to identify, use model from roboflow to make a prediction '''
def predict_pill_from_image_path(image_path=TEST_IMAGE_PATH):
    # Retrieve pill identification model
    rf = Roboflow(api_key=ROBOFLOW_API_KEY_PRIVATE)
    project = rf.workspace().project(RF_PROJECT_NAME)
    model = project.version(1).model

    prediction = model.predict(image_path, confidence=30, overlap=30)
    return prediction.json()


@app.route('/identify-pill', methods=['POST'])
def identify_pill():
    if 'image' not in request.files:
        return jsonify({'error': f'Must attach an image to the request: {list(request.files.items())}'}), 400

    # Get the uploaded image from the request and store locally
    uploaded_image = request.files['image']
    app.config['UPLOAD_FOLDER'] = 'images'
    temp_filename = tempfile.mktemp(suffix=".jpg", dir=app.config['UPLOAD_FOLDER'])
    uploaded_image.save(temp_filename)

    prediction_json = predict_pill_from_image_path(temp_filename)
    os.remove(temp_filename)

    return prediction_json


if __name__ == '__main__':
    app.run()
