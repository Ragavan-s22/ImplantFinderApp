from flask import Flask, request, render_template, redirect, jsonify, url_for
import tensorflow as tf
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import numpy as np
import os
from tensorflow.keras.layers import DepthwiseConv2D as BaseDepthwiseConv2D
from tensorflow.keras.utils import get_custom_objects

class CustomDepthwiseConv2D(BaseDepthwiseConv2D):
    def __init__(self, *args, **kwargs):
        kwargs.pop('groups', None)  # Remove unsupported argument
        super().__init__(*args, **kwargs)

get_custom_objects().update({'DepthwiseConv2D': CustomDepthwiseConv2D})

# Initialize the Flask application
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif'}

# Load the trained model
model_path = r"model/my_updated_model1.h5"
model = tf.keras.models.load_model(model_path)

# Compile the model (in case it's needed)
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Define class labels
class_labels = ['Cofield', 'Depuy', 'Tornier', 'Zimmer']  # Update to your actual class labels

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

def prepare_image(image_path):
    img = load_img(image_path, target_size=(224, 224))  # Match target_size to model input
    img = img_to_array(img)
    img = np.expand_dims(img, axis=0)
    img = img / 255.0
    return img

@app.route('/login', methods=['GET', 'POST'])
def sign_in():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        if email == 'admin@gmail.com' and password == '1234':
            return redirect(url_for('home'))
        else:
            return render_template('sign_in.html', error='Invalid email or password')
    return render_template('sign_in.html')

@app.route('/home', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/', methods=['GET', 'POST'])
def upload_and_predict():
    if request.method == 'POST':
        if 'file' not in request.files:
            return jsonify({'error': 'No file part in the request'}), 400

        file = request.files['file']
        if file.filename == '':
            return jsonify({'error': 'No selected file'}), 400

        if file and allowed_file(file.filename):
            if not os.path.exists(app.config['UPLOAD_FOLDER']):
                os.makedirs(app.config['UPLOAD_FOLDER'])

            filename = file.filename
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)

            img = prepare_image(file_path)
            prediction = model.predict(img)
            class_index = np.argmax(prediction[0])
            predicted_class = class_labels[class_index]

            return jsonify({'filename': filename, 'predicted_class': predicted_class})

    # Redirect to sign-in page if accessed without being logged in
    return redirect(url_for('sign_in'))

if __name__ == "__main__":
    app.run(debug=True)
