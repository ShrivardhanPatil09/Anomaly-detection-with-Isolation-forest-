import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs

X, y_true = make_blobs(n_samples=1000, centers=4, cluster_std=1.0, random_state=42)

k = 4 
kmeans = KMeans(n_clusters=k, random_state=0)
labels = kmeans.fit_predict(X)

print("Cluster assignments for first 10 points:")
for i in range(10):
    print(f"Point {X[i]}  Cluster {labels[i]}")

plt.figure(figsize=(10, 6))
plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='tab10', s=30, label='Data Points')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1],
            color='red', marker='X', s=200, label='Centroids')

plt.title("K-Means Clustering on Large Dataset")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.legend()
plt.grid(True)
plt.show()
