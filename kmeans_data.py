import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs

# Step 1: Generate large synthetic data (1000 points, 4 clusters)
X, y_true = make_blobs(n_samples=1000, centers=4, cluster_std=1.0, random_state=42)

# Step 2: Apply KMeans
k = 4  # Number of clusters
kmeans = KMeans(n_clusters=k, random_state=0)
labels = kmeans.fit_predict(X)

# Step 3: Print sample results
print("📌 Cluster assignments for first 10 points:")
for i in range(10):
    print(f"Point {X[i]} → Cluster {labels[i]}")

# Step 4: Plot the clusters
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
