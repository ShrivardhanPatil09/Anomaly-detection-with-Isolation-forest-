import pandas as pd
import os
from sklearn.ensemble import IsolationForest
import matplotlib.pyplot as plt
import seaborn as sns

file_path = r"D:\cradit_fraud\credit card fraud.csv"
df = pd.read_csv(file_path)

feature_column = 'credit_card_limit'

model = IsolationForest(contamination=0.1, random_state=42)
df['anomaly'] = model.fit_predict(df[[feature_column]])

anomalies = df[df['anomaly'] == -1]
normal = df[df['anomaly'] == 1]

print("\nAnomalies Detected:")
print(anomalies)

df.to_csv("anomaly_detection_result.csv", index=False)
