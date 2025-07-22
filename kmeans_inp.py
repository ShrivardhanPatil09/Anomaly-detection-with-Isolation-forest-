import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

raw_input = input("Enter 2D points like this x1,y1 x2,y2 x3,y3 : ")

try:
    points = []
    for pair in raw_input.strip().split():
        x, y = map(float, pair.split(','))
        points.append([x, y])

    X = np.array(points)

    k = int(input("Enter number of clusters (K): "))

    kmeans = KMeans(n_clusters=k, random_state=0)
    labels = kmeans.fit_predict(X)

    print("\nCluster Results:")
    for i in range(len(X)):
        print(f"Point {X[i]} → Cluster {labels[i]}")

    plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='tab10', s=100, label="Points")
    plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1],
                color='red', marker='X', s=200, label='Centroids')
    plt.title("K-Means Clustering from User Input")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid(True)
    plt.legend()
    plt.show()

except Exception as e:
    print("Invalid input format. Please use: x1,y1 x2,y2 x3,y3 ...")
