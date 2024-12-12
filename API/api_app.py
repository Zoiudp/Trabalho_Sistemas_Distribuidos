# Flask app code (api_app.py)
from flask import Flask, jsonify
from inference_yolo import predict_disease
from flask import request

app = Flask(__name__)

@app.route('/inferencia', methods=['GET'])
def get_data():

    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    if file:
        image_path = f'/tmp/{file.filename}'
        file.save(image_path)
    model_path = 'Pre_processing&Model_Training\coffee_disease_model.pt'
    conf_threshold = 0.8

    result = predict_disease(image_path, model_path, conf_threshold, display_image=False)

    return jsonify(result)
  

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
