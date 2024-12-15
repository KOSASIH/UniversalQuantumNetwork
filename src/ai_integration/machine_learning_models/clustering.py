import numpy as np
from sklearn.cluster import KMeans

class Clustering:
    def __init__(self, n_clusters):
        self.model = KMeans(n_clusters=n_clusters)

    def fit(self, data):
        """Fit the clustering model to the data."""
        self.model.fit(data)

    def predict(self, data):
        """Predict cluster labels for the data."""
        return self.model.predict(data)

if __name__ == "__main__":
    # Example usage
    data = np.random.rand(100, 2)  # Generate random data
    clustering = Clustering(n_clusters=3)
    clustering.fit(data)
    labels = clustering.predict(data)
    print("Cluster Labels:", labels)
