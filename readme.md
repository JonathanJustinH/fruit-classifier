# Fruit Freshness Classifier Streamlit App
# https://fruitclassifierbeta.streamlit.app/
A simple local Streamlit application that uses a Keras MobileNetV2 model to classify the freshness of fruits into **fresh**, **mild**, or **rotten**.

---

## Features

* Upload an image of a fruit and get a real-time classification.
* Detailed UI showing:

  * Freshness label (`fresh`, `mild`, `rotten`)
  * Confidence score
  * Icon and recommendation text

---

## Installation & Setup

1. **Clone the repository**

   ```bash
   git clone https://github.com/your-username/fruit-freshness-streamlit.git
   cd fruit-freshness-streamlit
   ```

2. **Create and activate a virtual environment** (recommended)

   ```bash
   python3 -m venv venv
   source venv/bin/activate   # macOS/Linux
   venv\\Scripts\\activate  # Windows
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Add your trained model**

   * Place your `model.h5` file in the project root.
   * Ensure `classify.py` points to the correct filename:

     ```python
     model = load_model("model.h5")
     ```

---

## Running Locally

1. **Start the app**

   ```bash
   streamlit run app.py
   ```

2. **Open in browser**

   * Visit `http://localhost:8501` to interact with the UI.

---

## Project Structure

```
fruit-freshness-streamlit/
├── app.py           # Main Streamlit script
├── classify.py      # Loads model and defines classify_fruit()
├── model.keras         # Keras MobileNetV2 weights
├── requirements.txt # Project dependencies
├── styles.css          # CSS
└── README.md        # This file
```

---

## Customization

* **CSS**: Edit `styles.css` to tweak card and icon styles.

---

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.
