from sklearn.cluster import DBSCAN
import numpy as np
import matplotlib.pyplot as plt

raw_input = input("Enter comma-separated numbers (e.g.y1,y2,y3,...,yn): ")
try:
    values = list(map(float, raw_input.strip().split(',')))
    if len(values) % 2 != 0:
        raise ValueError("Odd number of values.")

    points = [values[i:i+2] for i in range(0, len(values), 2)]
    X = np.array(points)
except:
    print("Invalid input. Please enter even number of comma-separated numbers like: 1,2,3,4")
    exit()

model = DBSCAN(eps=5, min_samples=2)
labels = model.fit_predict(X)

print("\nCluster Labels:")
for i, label in enumerate(labels):
    print(f"Point {X[i]} -> Cluster {label}")

for label in set(labels):
    color = 'k' if label == -1 else None
    cluster = X[labels == label]
    plt.scatter(cluster[:, 0], cluster[:, 1], s=100, label=f"Cluster {label}", color=color)

plt.title("DBSCAN Clustering Result")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)
plt.legend()
plt.show()
