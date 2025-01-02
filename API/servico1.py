# Flask app code (api_app.py)
import os
from flask import Flask, jsonify
from inference_yolo import predict_disease
from flask import request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/inferencia_image', methods=['POST'])
def get_data():

    file = request.files['photo']
    image_path = r'images/image_uploaded.jpg'
    
    # Ensure the directory exists
    os.makedirs('images', exist_ok=True)
    
    file.save(image_path)
    
    model_path = r'Pre_processing&Model_Training\coffee_disease_model.pt'
    conf_threshold = 0.8

    result = predict_disease(image_path, model_path, conf_threshold, display_image=False)
    return jsonify({'Disease detected': result.get('class_name'),
                    'Confidence': str(result.get('confidence')),
                    'chat': result.get('description')})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
