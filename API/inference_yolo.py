import cv2
from ultralytics import YOLO
from pathlib import Path
import numpy as np
from ollama import Client

from matplotlib import pyplot as plt

# Define function to predict coffee leaf disease
def predict_disease(
    image_path=None,
    model_path='coffee_disease_model.pt',
    conf_threshold=0.8,
    display_image=True,
    no_image=False,
    chat_message=None
):
    """
    Predict coffee leaf disease using trained YOLO model.
    
    Args:
        image_path (str): Path to the image file
        model_path (str): Path to the trained model weights
        conf_threshold (float): Confidence threshold for predictions
    
    Returns:
        dict: Dictionary containing prediction results
            {
                'class_name': str,
                'confidence': float,
                'image_path': str
            }
    """
    try:
        if(no_image!=True):
            # Check if image exists
            if not Path(image_path).exists():
                raise FileNotFoundError(f"Image not found: {image_path}")
                
            # Check if model exists
            if not Path(model_path).exists():
                raise FileNotFoundError(f"Model not found: {model_path}")
                
            # Load model
            model = YOLO(model_path)
            
            # Make prediction
            results = model.predict(
                source=image_path,
                conf=conf_threshold,
                save=False  # Set to True if you want to save annotated images
            )
            
            # Get the prediction results
            result = results[0]  # Get first result (single image)
            

            # if display_image:
            #     # Load and convert original image to RGB
            #     original_img = cv2.imread(image_path)
            #     original_img_rgb = cv2.cvtColor(original_img, cv2.COLOR_BGR2RGB)
                
            #     # Get annotated image and convert to RGB
            #     annotated_frame = result.plot()
            #     annotated_frame_rgb = cv2.cvtColor(annotated_frame, cv2.COLOR_BGR2RGB)
                
            #     # Create figure with two subplots side by side
            #     plt.figure(figsize=(20, 10))
                
            #     # Display original image
            #     plt.subplot(1, 2, 1)
            #     plt.imshow(original_img_rgb)
            #     plt.title('Original Image')
            #     plt.axis('off')
                
            #     # Display annotated image
            #     plt.subplot(1, 2, 2)
            #     plt.imshow(annotated_frame_rgb)
            #     plt.title('Detected Disease')
            #     plt.axis('off')
                
            #     plt.tight_layout()
            #     plt.show()
                

            
            # Get the class name and confidence
            class_id = int(result.probs.top1)  # Get predicted class index
            confidence = float(result.probs.top1conf)  # Get confidence score
            class_name = result.names[class_id]  # Get class name
            if (class_name == 'rust_xml_image'):
                class_name = 'Coffee Rust'
            elif (class_name == 'miner_img_xml'):
                class_name = 'Bicho Mineiro'
        # Create Ollama client and generate description
            client = Client(host='http://localhost:11434')
            prompt = f"Descreva a doença desse pé de café '{class_name}' e como tratar em poucas linhas."
            chat = client.generate(model='llama3.2', prompt=prompt)
            chat= chat['response'].replace('\n', ' ').replace('.', '').strip()
            
        else:
        
            # Create Ollama client and generate description
            client = Client(host='http://localhost:11434')
            chat = client.generate(model='llama3.2', prompt=chat_message)
            chat = chat['response'].replace('\n', ' ').replace('.', '').strip()

        return {
            'class_name': class_name,
            'confidence': round(confidence, 4),
            'image_path': image_path,
            'description': chat
        }
        
    except Exception as e:
        return {
            'error': str(e),
            'image_path': image_path
        }

# Example usage
if __name__ == "__main__":
    # Single image prediction
    result = predict_disease('bicho-mineiro.png')
    
    if 'error' in result:
        print(f"Error: {result['error']}")
    else:
        print(f"Image: {result['image_path']}")
        print(f"Predicted Disease: {result['class_name']}")
        print(f"Confidence: {result['confidence']:.2%}")
    
    # Example of batch prediction
    image_paths = [
        'bicho-mineiro.png',
    ]
    
    for img_path in image_paths:
        result = predict_disease(img_path)
        if 'error' in result:
            print(f"\nError processing {img_path}: {result['error']}")
        else:
            print(f"\nImage: {result['image_path']}")
            print(f"Predicted Disease: {result['class_name']}")
            print(f"Confidence: {result['confidence']:.2%}")
            
   
