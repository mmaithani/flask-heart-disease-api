import pickle
from flask import Flask, request, render_template
import pandas as pd
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)

# Load the pre-trained model and scaler
model = pickle.load(open('model.pkl', 'rb'))
scaler = pickle.load(open('scaler.pkl', 'rb'))

# Route to serve the prediction form (GET request)
@app.route('/')
def home():
    return render_template('index.html')  # This will render the form

# Route to make predictions (POST request)
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get the data from the form submission (using request.form)
        data = {
            'age': float(request.form['age']),
            'sex': int(request.form['sex']),
            'cp': int(request.form['cp']),
            'trestbps': int(request.form['trestbps']),
            'chol': int(request.form['chol']),
            'fbs': int(request.form['fbs']),
            'restecg': int(request.form['restecg']),
            'thalach': int(request.form['thalach']),
            'exang': int(request.form['exang']),
            'oldpeak': float(request.form['oldpeak']),
            'slope': int(request.form['slope']),
            'ca': int(request.form['ca']),
            'thal': int(request.form['thal'])
        }

        # Convert input data into DataFrame
        input_data = pd.DataFrame([data])

        # Preprocess the input data (apply scaler)
        scaled_data = scaler.transform(input_data)

        # Predict using the model
        prediction = model.predict(scaled_data)

        # Convert prediction to readable result
        prediction_result = "Heart Disease" if prediction[0] == 1 else "No Heart Disease"

        # Return the result along with the form (render the form with prediction result)
        return render_template('index.html', prediction=prediction_result)

    except Exception as e:
        # If something goes wrong, return the error
        return render_template('index.html', prediction=f"Error: {str(e)}")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
