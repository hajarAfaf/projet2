%%writefile README.md
# MNIST Handwritten Digit Recognizer 🧠✍️
# 🧠 Deep Learning Lab - DL Deployment avec Streamlit

This project is part of the Deep Learning Lab (Project 2) for the Master IT program at Université Mohammed V.

## 🎯 Goal

Create a web-based application using **Streamlit** to recognize handwritten digits...

## 👥 Team Members
- AFAF Hajar
- EZZERROUTI Salwa

## 🎓 Project Supervisor
This project was carried out under the supervision of **Professor Mahmoudi Abdelhak**, Faculty of Sciences.

## 📦 Repository Contents
- `notebook.ipynb` : Notebook containing the model training code.
- `app.py` :  Streamlit application for testing the model.
- `requirements.txt` : List of dependencies.
- `video/demo.mp4` : 7-minute presentation explaining the code and environment.
- `README.md` : This documentation file.

## Google Collab link:
https://colab.research.google.com/drive/1ufcxw3ROhPcKQLfpMh64k4VL56FBAe90?usp=

## Video Link:
https://drive.google.com/file/d/1pQBBDLfWSJV1kFnzfQlEnzqEA0fi1hKD/view?usp=sharing

## 🛠️Tools & Technologies

- TensorFlow / Keras
- Streamlit
- OpenCV
- Ngrok
- Python

## 🔍Model Training

- Dataset: MNIST (70,000 handwritten digits)
-Architecture:
Flatten → Dense(128, ReLU) → Dense(10, Softmax)

## 🔧 Environment Setup:

#### For Windows :
```bash
git clone <URL_DU_DEPOT>
cd DL-deployment
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py

#### For Linux/macOS :
git clone <URL_DU_DEPOT>
cd DL-deployment
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
streamlit run app.py




