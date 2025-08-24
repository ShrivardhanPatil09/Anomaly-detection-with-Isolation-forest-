import matplotlib.pyplot as plt

raw = input("Enter time series data (comma-separated, e.g. 10,12,14,16): ")

try:
    data = list(map(float, raw.strip().split(',')))
except:
    print("Invalid input. Use comma-separated numbers.")
    exit()

window_size = 3  
if len(data) < window_size:
    print(f"Need at least {window_size} values.")
    exit()

forecast_steps = int(input("How many future points to forecast? "))
forecast = []

for _ in range(forecast_steps):
    window = data[-window_size:]
    avg = sum(window) / window_size
    forecast.append(avg)
    data.append(avg) 

print("\nForecasted values:", forecast)

# Plot original + forecast
plt.plot(range(len(data)), data, marker='o', label='Original + Forecast')
plt.axvline(x=len(data)-forecast_steps-1, color='gray', linestyle='--', label="Forecast Start")
plt.title("Simple Moving Average Forecast")
plt.xlabel("Time Step")
plt.ylabel("Value")
plt.grid(True)
plt.legend()
plt.show()
