# 🚀 Heart Disease Prediction API

Welcome to the **Heart Disease Prediction API**, a Flask-based microservice designed to predict the likelihood of heart disease using a machine learning model. This project is powered by **Random Forest Classification**, and the model has been trained on clinical patient data.

![Heart Health](https://source.unsplash.com/1600x900/?health,doctor,heart)

## 🌟 Features
✅ **Predicts heart disease risk** using real clinical parameters  
✅ **RESTful API** built with Flask  
✅ **Machine Learning Model** trained using Random Forest Classifier  
✅ **Scalable Deployment** using Gunicorn & Flask-RESTful  
✅ **Preprocessed Input Data** with StandardScaler  
✅ **Interactive Frontend Form** for easy predictions  

---

## 🏗️ Project Structure
```
📂 flask-heart-disease-api
│-- 📂 static              # Static assets (CSS, JS, images)
│-- 📂 templates           # Frontend HTML files
│-- 📄 app.py              # Main Flask API
│-- 📄 train_model.py      # Script to train & save ML model
│-- 📄 requirements.txt    # Dependencies
│-- 📄 README.md           # Project documentation
│-- 📄 heart.csv           # Dataset used for training
│-- 📄 model.pkl           # Trained ML model
│-- 📄 scaler.pkl          # Standard Scaler object
```

---

## 🛠️ Installation & Setup
### 🔹 1. Clone the Repository
```sh
git clone https://github.com/yourusername/flask-heart-disease-api.git
cd flask-heart-disease-api
```
### 🔹 2. Create a Virtual Environment & Install Dependencies
```sh
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate    # On Windows
pip install -r requirements.txt
```
### 🔹 3. Run the Flask API
```sh
python app.py
```
By default, the API runs at `http://127.0.0.1:5000/`

---

## 🎯 API Usage
### 🔹 **1. Predict Heart Disease (POST Request)**
**Endpoint:** `/predict`  
**Content-Type:** `application/json`  

#### 📥 Example Request:
```json
{
  "age": 55,
  "sex": 1,
  "cp": 2,
  "trestbps": 130,
  "chol": 250,
  "fbs": 0,
  "restecg": 1,
  "thalach": 150,
  "exang": 1,
  "oldpeak": 2.5,
  "slope": 1,
  "ca": 2,
  "thal": 3
}
```

#### 📤 Example Response:
```json
{
  "prediction": "Heart Disease",
  "probability": 0.85
}
```

---

## 🎨 Frontend Form
This project includes an interactive **HTML form** for easy predictions. Just open `index.html` in your browser, fill in the details, and get instant results!  

---

## 🚀 Deployment (Optional)
You can deploy this project on **Render, AWS, or Heroku** using **Gunicorn**.
```sh
gunicorn app:app -b 0.0.0.0:8000
```

---

## 📝 License
This project is **open-source** and free to use. Feel free to contribute or improve! 💡

🔗 **Connect with me:** [LinkedIn](https://www.linkedin.com/in/rahulroy0499/) | [GitHub](https://github.com/rahul-roy56)  
📩 **Contact:** your-email@example.com

💖 _Stay heart-healthy and keep coding!_ 🚀

