from fastapi import FastAPI, File, UploadFile
from tensorflow.keras.models import load_model
from PIL import Image
import numpy as np
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

app = FastAPI()

# Load the pre-trained Keras model
model = load_model("new_model.keras")

# Define the list of celebrities
celebrities = ['Angelina Jolie', 'Brad Pitt', 'Hugh Jackman', 'Johnny Depp', 'Leonardo DiCaprio']

# Preprocess the uploaded image
def preprocess_image(image: Image.Image) -> np.array:
    # Resize the image to the input size expected by your model (e.g., 150x150)
    image = image.resize((100, 100))
    # Convert the image to a numpy array and normalize it
    image = np.array(image) / 255.0
    # Add batch dimension
    image = np.expand_dims(image, axis=0)
    return image

@app.get("/")
async def read_root():
    return {
        "message": "Welcome to the Celebrity Prediction API!",
        "available_celebrities": celebrities
    }

@app.post("/predict/")
async def predict(file: UploadFile = File(...)):
    # Read the uploaded file and convert it to an image
    img = Image.open(file.file)
    # Preprocess the image for model input
    img_array = preprocess_image(img)
    # Predict the celebrity
    predictions = model.predict(img_array)
    # Get the index of the highest probability
    predicted_index = np.argmax(predictions)
    # Get the celebrity name
    predicted_celebrity = celebrities[predicted_index]
    return {"celebrity": predicted_celebrity}

if __name__ == "__main__":
   uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
