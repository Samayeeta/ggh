import tensorflow as tf
from tensorflow.keras import layers, models
import numpy as np
import cv2
import os

def create_and_save_model(image_path, model_path):
    images = []
    labels = []
    for filename in os.listdir(image_path):
        if filename.endswith(('.jpg', '.jpeg', '.png')):
            img_path = os.path.join(image_path, filename)
            img = cv2.imread(img_path)
            if img is None:
                print(f"Error loading image: {filename}")
                continue
            img = cv2.resize(img, (128, 128))
            img = img / 255.0
            images.append(img)
            labels.append(0)  # Placeholder label

    if not images:
        print("No images were loaded. Exiting.")
        return

    images = np.array(images)
    labels = np.array(labels)

    model = models.Sequential([
        layers.Conv2D(32, (3, 3), activation='relu', input_shape=(128, 128, 3)),
        layers.MaxPooling2D((2, 2)),
        layers.Conv2D(64, (3, 3), activation='relu'),
        layers.MaxPooling2D((2, 2)),
        layers.Conv2D(128, (3, 3), activation='relu'),
        layers.MaxPooling2D((2, 2)),
        layers.Flatten(),
        layers.Dense(128, activation='relu'),
        layers.Dense(1, activation='sigmoid')
    ])

    model.compile(optimizer='adam',
                  loss='binary_crossentropy',
                  metrics=['accuracy'])

    model.fit(images, labels, epochs=1)

    model.save(model_path)
    print(f"Model saved to: {model_path}")

data_path = os.path.join(os.getcwd(), "data/")
model_path = os.path.join(os.getcwd(), "models/cic_cnn.h5")
create_and_save_model(data_path, model_path)