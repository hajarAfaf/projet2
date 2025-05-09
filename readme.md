%%writefile README.md
# MNIST Handwritten Digit Recognizer 🧠✍️
# 🧠 Deep Learning Lab - DL Deployment avec Streamlit

This project is part of the Deep Learning Lab (Project 2) for the Master IT program at Université Mohammed V.

## 🎯 Goal

Create a web-based application using **Streamlit** to recognize handwritten digits...

## 📦 Contenu du dépôt
- `notebook.ipynb` : Notebook contenant le code d’entraînement du modèle.
- `app.py` : Application Streamlit pour tester le modèle.
- `requirements.txt` : Liste des dépendances.
- `video/demo.mp4` : Présentation de 7 min expliquant le code et l’environnement.
- `README.md` : Ce fichier de documentation.

## Lien Google Collab:
https://colab.research.google.com/drive/1ufcxw3ROhPcKQLfpMh64k4VL56FBAe90?usp=sharing
https://colab.research.google.com/drive/1ufcxw3ROhPcKQLfpMh64k4VL56FBAe90?pli=1&authuser=1#scrollTo=hDjPAI8l_E5i

## 🔧 Configuration de l’environnement

#### Pour Windows :
```bash
git clone <URL_DU_DEPOT>
cd DL-deployment
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py

#### Pour Linux/macOS :

git clone <URL_DU_DEPOT>
cd DL-deployment
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
streamlit run app.py


