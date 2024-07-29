from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.preprocessing import image
from tensorflow.keras.optimizers import RMSprop
import tensorflow as tf
import os
import numpy as np

# Load and preprocess the image data
train = ImageDataGenerator(rescale=1/255)
validation = ImageDataGenerator(rescale=1/255)

train_dataset = train.flow_from_directory("E:/Ragav/Intern/Implantdetection/computer-vision/basedata/training/",
                                          target_size=(200,200),
                                          batch_size=3,
                                          class_mode='binary')

validation_dataset = validation.flow_from_directory("E:/Ragav/Intern/Implantdetection/computer-vision/basedata/validation/",
                                                    target_size=(200,200),
                                                    batch_size=3,
                                                    class_mode='binary')

# Build the model
model = tf.keras.models.Sequential([
    tf.keras.layers.Conv2D(16, (3, 3), activation='relu', input_shape=(200, 200, 3)),
    tf.keras.layers.MaxPool2D(2, 2),
    tf.keras.layers.Conv2D(16, (3, 3), activation='relu'),
    tf.keras.layers.MaxPool2D(2, 2),
    tf.keras.layers.Conv2D(16, (3, 3), activation='relu'),
    tf.keras.layers.MaxPool2D(2, 2),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(512, activation='relu'),
    tf.keras.layers.Dense(1, activation='sigmoid')
])

# Compile the model
model.compile(loss='binary_crossentropy',
              optimizer=RMSprop(learning_rate=0.001),
              metrics=['accuracy'])

# Train the model
model_fit = model.fit(train_dataset,
                      steps_per_epoch=5,
                      epochs=40,
                      validation_data=validation_dataset)

# Save the model
model_save_path = "E:/Ragav/Intern/Implantdetection/cnn_model.keras"
model.save(model_save_path)
print(f"Model saved to {model_save_path}")
