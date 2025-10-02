from flask import Flask, render_template, request, jsonify
import pandas as pd
import numpy as np
import pickle

app = Flask(__name__)

# --- FILE PATHS ---
CAR_DATA_PATH = 'ar price linear\Cleaned_Car_data.csv'
MODEL_PATH = 'car price linear\Cleaned_Car_data.csv'
# ------------------

# Load Model + Preprocessor
try:
    car = pd.read_csv(CAR_DATA_PATH).drop(columns=['Unnamed: 0'], errors='ignore')
    with open(MODEL_PATH, 'rb') as f:
        saved_data = pickle.load(f)
        model = saved_data["model"]
        preprocessor = saved_data["preprocessor"]
except FileNotFoundError:
    print(f"Error: Required file not found. Check paths: {CAR_DATA_PATH} or {MODEL_PATH}")
    car = pd.DataFrame({'company': [], 'name': [], 'year': [], 'fuel_type': [], 'kms_driven': [], 'Price': []})
    model, preprocessor = None, None


# ------------------ ROUTES ------------------

@app.route('/', methods=['GET','POST'])
def index():
    companies = sorted(car['company'].unique())
    car_models = sorted(car['name'].unique())
    year = sorted(car['year'].unique(), reverse=True)
    fuel_type = sorted(car['fuel_type'].unique())

    companies.insert(0, 'Select Company')  # default option

    return render_template('index.html',
                           companies=companies,
                           car_models=car_models,
                           years=year,
                           fuel_types=fuel_type)


# --- AJAX: Get models by company ---
@app.route('/car_models', methods=['GET'])
def car_models_by_company():
    company = request.args.get('company')
    if company:
        filtered_models = sorted(car[car['company'] == company]['name'].unique())
        return jsonify({'car_models': filtered_models})
    return jsonify({'car_models': []})


# --- Prediction ---
@app.route('/predict', methods=['POST'])
def predict():
    if model is None or preprocessor is None:
        return jsonify({'error': 'Prediction model failed to load.'}), 500

    try:
        # Extract form data
        company = request.form.get('company')
        car_model = request.form.get('car_model')
        year = int(request.form.get('year'))
        fuel_type = request.form.get('fuel_type')
        kms_driven = int(request.form.get('kms_driven'))

        if not all([company, car_model, year, fuel_type, kms_driven is not None]):
            return jsonify({'error': 'Missing required form data.'}), 400

        # Prepare DataFrame
        prediction_data = pd.DataFrame([[car_model, company, year, kms_driven, fuel_type]],
                                       columns=['name', 'company', 'year', 'kms_driven', 'fuel_type'])

        # --- FIX: Add dummy Unnamed: 0 column if missing ---
        if 'Unnamed: 0' not in prediction_data.columns:
            prediction_data['Unnamed: 0'] = 0

        # Transform using the same preprocessor
        X_processed = preprocessor.transform(prediction_data)

        # Predict
        prediction = model.predict(X_processed)
        predicted_price = np.round(prediction[0], 2)

        # Ensure non-negative
        if predicted_price < 0:
            predicted_price = 100

        formatted_price = f"₹ {predicted_price:,.2f}"

        return jsonify({'prediction': formatted_price})

    except Exception as e:
        print(f"Prediction Error: {e}")
        return jsonify({'error': 'An unexpected error occurred during prediction.'}), 500


# ------------------ MAIN ------------------
if __name__ == "__main__":
    app.run()
