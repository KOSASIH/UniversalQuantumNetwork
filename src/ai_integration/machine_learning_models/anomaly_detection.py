import numpy as np
from sklearn.ensemble import IsolationForest

class AnomalyDetection:
    def __init__(self):
        self.model = IsolationForest()

    def fit(self, data):
        """Fit the model to the data."""
        self.model.fit(data)

    def predict(self, data):
        """Predict anomalies in the data."""
        return self.model.predict(data)

if __name__ == "__main__":
    # Example usage
    data = np.random.rand(100, 2)  # Generate random data
    anomaly_detector = AnomalyDetection()
    anomaly_detector.fit(data)
    predictions = anomaly_detector.predict(data)
    print("Anomaly Predictions:", predictions)
