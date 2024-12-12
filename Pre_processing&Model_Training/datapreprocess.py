import os
import shutil
import random

def create_dir_structure(base_dir, classes):
    for split in ['train', 'val']:
        for cls in classes:
            os.makedirs(os.path.join(base_dir, split, cls), exist_ok=True)

def split_dataset(source_dir, dest_dir, split_ratio=0.8):
    classes = [d for d in os.listdir(source_dir) if os.path.isdir(os.path.join(source_dir, d))]
    create_dir_structure(dest_dir, classes)

    for cls in classes:
        class_dir = os.path.join(source_dir, cls)
        images = [f for f in os.listdir(class_dir) if f.endswith('.jpg')]
        random.shuffle(images)
        
        split_point = int(len(images) * split_ratio)
        train_images = images[:split_point]
        val_images = images[split_point:]

        for img in train_images:
            shutil.copy(os.path.join(class_dir, img), os.path.join(dest_dir, 'train', cls, img))
        
        for img in val_images:
            shutil.copy(os.path.join(class_dir, img), os.path.join(dest_dir, 'val', cls, img))

if __name__ == "__main__":
    source_directory = 'dataset'
    destination_directory = 'dataset_split'
    split_ratio = 0.8  # 80% training, 20% validation

    split_dataset(source_directory, destination_directory, split_ratio)