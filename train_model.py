import pandas as pd
import pickle
from sklearn.linear_model import LinearRegression
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder

# Load your cleaned dataset
df = pd.read_csv("C:/Users/SOHAIB ALAM/OneDrive/Desktop/scaler/Project/car price linear/Cleaned_Car_data.csv")

# Features and target
X = df.drop(columns=['Price'])
y = df['Price']

# Preprocessing: OneHotEncode categorical variables
preprocessor = ColumnTransformer(
    transformers=[
        ('ohe', OneHotEncoder(handle_unknown='ignore'), ['name', 'company', 'fuel_type'])
    ],
    remainder='passthrough'
)

# Fit and transform
X_processed = preprocessor.fit_transform(X)

# Train model
model = LinearRegression()
model.fit(X_processed, y)

# Save both model + preprocessor together
with open("C:/Users/SOHAIB ALAM/OneDrive/Desktop/scaler/Project/car price linear/LinearRegressionModel.pkl", "wb") as f:
    pickle.dump({"model": model, "preprocessor": preprocessor}, f)

print("✅ Model trained and saved successfully!")
