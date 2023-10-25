from flask import Flask, request, render_template
import cv2
import numpy as np
from keras.models import load_model

app = Flask(__name__)

# Load the model
model = load_model("keras_Model.h5", compile=False)

# Load the labels
class_names = open("labels.txt", "r").readlines()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get the uploaded image from the form
    image = request.files['image']

    # Read and preprocess the image
    image = cv2.imdecode(np.fromstring(image.read(), np.uint8), cv2.IMREAD_COLOR)
    image = cv2.resize(image, (224, 224), interpolation=cv2.INTER_AREA)
    image = np.asarray(image, dtype=np.float32).reshape(1, 224, 224, 3)
    image = (image / 127.5) - 1

    # Predict the class
    prediction = model.predict(image)
    index = np.argmax(prediction)
    confidence_score = np.round(prediction[0][index] * 100)

    if confidence_score < 50:  # Adjust the threshold as needed
        class_name = "Invalid"
    else:
        class_name = class_names[index]

    return render_template('results.html', class_name=class_name, confidence=confidence_score)

if __name__ == '__main__':
    app.run(debug=True)
