import flask_restful
from flask import Flask, request, jsonify
from flask_restful import Resource, Api
import numpy as np
import tensorflow as tf


app = Flask(__name__)
api = Api(app)

@app.route('/ping', methods=['GET'])
def ping():
    return jsonify({'status': 'running'})

CLASS_NAMES = ['Pepper__bell___Bacterial_spot',
 'Pepper__bell___healthy',
 'Potato___Early_blight',
 'Potato___Late_blight',
 'Potato___healthy',
 'Tomato_Bacterial_spot',
 'Tomato_Early_blight',
 'Tomato_Late_blight',
 'Tomato_Leaf_Mold',
 'Tomato_Septoria_leaf_spot',
 'Tomato_Spider_mites_Two_spotted_spider_mite',
 'Tomato__Target_Spot',
 'Tomato__Tomato_YellowLeaf__Curl_Virus',
 'Tomato__Tomato_mosaic_virus',
 'Tomato_healthy']    

@app.route('/predict', methods=['POST'])
def predict():
    image = request.files['file']
    image = np.array(image.open(image))

    img_batch = np.expand_dims(image, 0)

    model = tf.keras.models.load_model("./models/1")
    predictions = model.predict(img_batch)
    predicted_class = CLASS_NAMES[np.argmax(predictions[0])]
    confidence = np.max(predictions[0])
    return jsonify({'class': predicted_class, 'confidence': float(confidence)})

if __name__ == "__main__":
    app.run(debug=True)
