import pandas as pd
from sklearn.ensemble import IsolationForest

file_path = r"D:\cradit_fraud\credit card fraud.csv"
df = pd.read_csv(file_path)

feature_column = 'credit_card_limit'
df[feature_column] = pd.to_numeric(df[feature_column], errors='coerce')
df = df.dropna(subset=[feature_column])

model = IsolationForest(contamination=0.1, random_state=42)
model.fit(df[[feature_column]])

try:
    user_value = float(input("Enter a credit card limit:"))
except ValueError:
    print("Invalid number, enter correct number")
    exit()

prediction = model.predict([[user_value]])

if prediction[0] == -1:
    print(f"The value {user_value} is an **Anomaly** (possibly fraudulent).")
else:
    print(f"The value {user_value} is **Normal**.")