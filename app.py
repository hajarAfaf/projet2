%%writefile app.py
import streamlit as st
from streamlit_drawable_canvas import st_canvas
import tensorflow as tf
import numpy as np
import cv2

#Chargement du modele et  Titre de l’application
new_model = tf.keras.models.load_model("model\model_mnist.keras")
st.title("MNIST Handwritten Digit Recognizer")

#Interface de dessin
canvas_result = st_canvas(
    fill_color="white",
    stroke_width=15,
    stroke_color="black",
    background_color="white",
    height=280,
    width=280,
    drawing_mode="freedraw",
    key="canvas"
)

#Traitement de l'image et prédiction
if canvas_result.image_data is not None:
    img = canvas_result.image_data
    img = cv2.cvtColor(img.astype('uint8'), cv2.COLOR_RGBA2GRAY)
    img = cv2.resize(img, (28, 28))
    img = 255 - img
    img = img / 255.0
    img = img.reshape(1, 28, 28)

    prediction = new_model.predict(img)
    st.write("### Predicted digit:", np.argmax(prediction))
#lancer ton application Streamlit et de la rendre accessible via un lien public
#obtenir authotoken et le poser
!ngrok config add-authtoken 
from pyngrok import ngrok
import time

# Kill previous tunnels if any
ngrok.kill()

# Start the Streamlit app in background (replace 'app.py' with your actual file name)
!streamlit run app.py &> /dev/null &

# Wait a bit for Streamlit to launch
time.sleep(5)

# Create the public tunnel
public_url = ngrok.connect("http://localhost:8501")
print("🌐 Your app is live at:", public_url)
