**🚗 Car Price Predictor**
----------------------------------------

<img width="875" height="840" alt="image" src="https://github.com/user-attachments/assets/29b80182-96f5-423e-be2c-1129c7be8f67" />


# 🧩 Project Overview

- **Objective:** Predict realistic resale prices for cars based on features like manufacturer, model, year, fuel type, and kilometers driven.  
- **Dataset:** Indian used cars dataset (cleaned for missing values and outliers).  
- **Machine Learning Model:** Linear Regression.  
- **Deployment:** Flask web app with dynamic AJAX-driven dropdowns.


## Features

- **Predict Car Prices**  
  Get accurate price predictions for used cars using a trained **Linear Regression model**.
- **Dynamic Dropdowns**  
  Select Manufacturer → Models update automatically using **AJAX**.
- **Responsive UI**  
  Beautifully designed using **Tailwind CSS** and mobile-friendly.
- **Realistic Data Handling**  
  Handles missing or negative values intelligently.
- **Fast & Lightweight**  
  No heavy frontend frameworks needed; simple and efficient.


## Tech Stack

- **Python** – Data cleaning, preprocessing, and ML  
- **Pandas / NumPy** – Data manipulation  
- **Scikit-Learn** – Preprocessing and Linear Regression  
- **Flask** – Backend web server  
- **JavaScript / AJAX** – Dynamic frontend behavior  
- **Tailwind CSS** – Responsive UI design  
- **GitHub & Heroku** – Version control & deployment

## 📊 Data Pipeline

1. **Load & Explore Data:**  
   - Check for missing values, duplicates, and column types.
2. **Data Cleaning:**  
   - Drop unnecessary columns (e.g., `Unnamed: 0`)  
   - Remove invalid entries and outliers  
   - Fill or correct missing numeric and categorical data  
3. **Feature Selection & Engineering:**  
   - Select relevant features: `company`, `name`, `year`, `fuel_type`, `kms_driven`  
   - Encode categorical variables and scale numeric features  
4. **Model Training:**  
   - Train **Linear Regression** on processed data  
   - Save trained model and preprocessor using **pickle**  
5. **Deployment:**  
   - Serve predictions via **Flask API**  
   - Dynamic AJAX-based frontend updates  



## How to use this project ?

1. Clone the repository:
   ```bash
   git clone https://github.com/iamZaid-Alam/car-price-prediction.git
   cd car-price-prediction

2. Create virtual environment and activate:
    ```bash
    python -m venv venv
    venv\Scripts\activate  # Windows
    source venv/bin/activate  # macOS/Linux

3. Install dependencies:
    ```bash
    pip install -r requirements.txt

4. Run the app:
   ```bash
    python app.py

5. Open in browser:
http://127.0.0.1:5000


**Note : You can deploy it on heroku also**
