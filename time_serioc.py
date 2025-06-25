import pandas as pd
import matplotlib.pyplot as plt

data = [30, 31, 29, 30, 75, 31, 32]
df = pd.DataFrame(data, columns=['temperature'])

df['rolling_mean'] = df['temperature'].rolling(window=3, center=True).mean()

df['anomaly'] = abs(df['temperature'] - df['rolling_mean']) > 10

print(df)

plt.plot(df['temperature'], label='Temperature')
plt.plot(df['rolling_mean'], label='Rolling Mean', linestyle='--')
plt.scatter(df.index[df['anomaly']], df['temperature'][df['anomaly']], color='red', label='Anomaly')
plt.legend()
plt.title("Anomaly Detection using Moving Average")
plt.show()
