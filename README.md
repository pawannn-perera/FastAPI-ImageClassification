# Celebrity Prediction API

This project is a FastAPI application that predicts the celebrity from an uploaded image using a Keras model. The model has been trained on a set of celebrity images and can classify images into one of the following celebrities:

- Angelina Jolie
- Brad Pitt
- Hugh Jackman
- Johnny Depp
- Leonardo DiCaprio

## Features

- Upload an image to the `/predict/` endpoint to receive a celebrity prediction.
- View the available celebrities at the root endpoint `/`.
  
## Requirements

- Python 3.8+
- FastAPI
- TensorFlow
- Pillow
