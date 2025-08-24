import matplotlib.pyplot as plt
from lifelines import KaplanMeierFitter

time_input = input("Type event times separated by commas (Ex., 5,6,6,2,4,8,10): ")
event_input = input("Type event happened? (1=Yes, 0=No) Ex., 1,0,1,1,1,0,1: ")

time = list(map(int, time_input.strip().split(',')))
event = list(map(int, event_input.strip().split(',')))

km = KaplanMeierFitter()
km.fit(time, event)

print("\nSurvival Table:")
print(km.survival_function_)

km.plot_survival_function()
    
plt.title("Survival Analysis (Kaplan-Meier Curve)")
plt.xlabel("Time")
plt.ylabel("Survival Probability")
plt.grid(True)
plt.show()
