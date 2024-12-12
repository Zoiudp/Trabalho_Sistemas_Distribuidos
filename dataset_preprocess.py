import os
import shutil
from sklearn.model_selection import train_test_split
import random

def create_train_val_split(source_dir, train_dir, val_dir, val_split=0.2):
    # Create main directories if they don't exist
    os.makedirs(train_dir, exist_ok=True)
    os.makedirs(val_dir, exist_ok=True)
    
    # Loop through each class directory
    for class_name in os.listdir(source_dir):
        class_dir = os.path.join(source_dir, class_name)
        if not os.path.isdir(class_dir):
            continue
            
        # Create class directories in train and val
        train_class_dir = os.path.join(train_dir, class_name)
        val_class_dir = os.path.join(val_dir, class_name)
        os.makedirs(train_class_dir, exist_ok=True)
        os.makedirs(val_class_dir, exist_ok=True)
        
        # Get all images in the class directory
        images = [f for f in os.listdir(class_dir) if f.endswith(('.jpg', '.jpeg', '.png'))]
        
        # Split into train and validation sets
        train_images, val_images = train_test_split(
            images, 
            test_size=val_split, 
            random_state=42
        )
        
        # Copy images to respective directories
        for img in train_images:
            src = os.path.join(class_dir, img)
            dst = os.path.join(train_class_dir, img)
            shutil.copy2(src, dst)
            
        for img in val_images:
            src = os.path.join(class_dir, img)
            dst = os.path.join(val_class_dir, img)
            shutil.copy2(src, dst)

# Usage example:
source_directory = "dataset"  # Your original dataset directory
train_directory = "dataset/train"
val_directory = "dataset/val"

create_train_val_split(source_directory, train_directory, val_directory, val_split=0.2)