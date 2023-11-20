from flask import Flask,render_template, request, jsonify
from predict_image import predict_pill_from_image_path
import time, tempfile
from flask_login import LoginManager, login_user, logout_user, login_required
from db_models import User, Pill, db, app
import os

@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route("/api/time")
def get_current_time():
    print('testing that endpoint was hit')
    return {'time': time.time()}

@app.route('/api/identify-pill', methods=['POST'])
def get_pill_info():
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

@app.route('/api/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        print(f"Got username: {username} password: {password}")
        user = User(username=username) 
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        return {'success': 'account created! jk nothing is going to happen'}

@app.route('/api/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username=username).first() 
        if user and user.check_password(password):
            login_user(user)
            return {'success': f'login successful, welcome {user.username}'}
        else: 
            return {'fail': 'login failed'}
    return render_template('index.html')


@app.route('/api/logout')
@login_required
def logout():
    logout_user()
    return {'success': 'logged out'}