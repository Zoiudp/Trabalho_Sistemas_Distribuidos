# Import the YOLO model from ultralytics library
from ultralytics import YOLO

# Initialize a pretrained YOLO classifier model
# yolov8n-cls.pt is a nano-sized classification model
model = YOLO('yolov8n-cls.pt')

# Train the YOLO model on our custom dataset with the following configuration:
results = model.train(
    data='dataset',              # Directory containing our training data
    epochs=20,                  # Train for 100 epochs to ensure good learning
    imgsz=640,                  # Input images will be resized to 640x640 pixels
    batch=8,                    # Process 8 images at a time during training
    device='cpu',                 # Use GPU device 0 for training
    project='coffee_disease',    # Save results under 'coffee_disease' project folder
    name='run1',                # This training run will be saved as 'run1'
    save=True,                  # Save the trained model weights
    plots=True                  # Generate training metrics plots
)

# Save the trained model
model.save('coffee_disease_model.pt')

