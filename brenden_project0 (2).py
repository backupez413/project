# -*- coding: utf-8 -*-
"""Brenden_Project0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1hf0H30l1EzEE0X8nBRPSWv7KG3LsSa0B
"""

from h5py._hl.filters import guess_chunk
from keras.models import load_model
from PIL import Image, ImageOps
import numpy as np
#import argparse

#Get input from the user
#parser = argparse.ArgumentParser()
#parser.add_argument("filename", type=str, help="filename of the image to process")
#opt = parser.parse_args()


model = load_model('keras_model.h5')


# Create the array of the right shape to feed into the keras model
# The 'length' or number of images you can put into the array is
# determined by the first position in the shape tuple, in this case 1.
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

image = Image.open('lostdog.jpg')


#resize the image to a 224x224 with the same strategy as in TM2:
#resizing the image to be at least 224x224 and then cropping from the center
size = (224, 224)
image = ImageOps.fit(image, size, Image.ANTIALIAS)

#turn the image into a numpy array
image_array = np.asarray(image)
# Normalize the image
normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
# Load the image into the array
data[0] = normalized_image_array

# run the inference
prediction = model.predict(data)
print("Confidence level in all classes: " + str(prediction))
greatest_guess = 0
index = 0
count = 0
for predictions in prediction:
  for guess in predictions:
    if guess > greatest_guess:
      greatest_guess = guess
      index = count
    count+= 1

classes = ["cars", "police cars"]
print("Class with greatest confidence was: " + str(classes[index]))
print("With a confidence of: " + str(greatest_guess))