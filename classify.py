import numpy as np
from PIL import Image
from tensorflow.keras.models import load_model
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
from tensorflow.keras.preprocessing.image import img_to_array

# Load your trained MobileNetV2 model (do this once, not inside the function ideally)
model = load_model("model.h5")

# Define your class labels
CLASS_NAMES = ["fresh", "mild", "rotten"]

def classify_fruit(image: Image.Image) -> dict:
    """
    Classify fruit freshness using trained MobileNetV2 model.
    """
    # Preprocess image
    target_size = (224, 224)  # MobileNetV2 default input size
    image = image.resize(target_size)
    img_array = img_to_array(image)
    img_array = preprocess_input(img_array)  # Normalize for MobileNetV2
    img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension

    # Predict
    predictions = model.predict(img_array)
    confidence = np.max(predictions)
    predicted_index = np.argmax(predictions)
    freshness_label = CLASS_NAMES[predicted_index]

    return {
        "freshness": freshness_label,
        "confidence": round(float(confidence) * 100, 2)
    }
