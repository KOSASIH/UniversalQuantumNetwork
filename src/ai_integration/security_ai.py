import numpy as np
from sklearn.ensemble import IsolationForest

class SecurityAI:
    def __init__(self):
        self.model = IsolationForest()

    def train(self, data):
        """Train the anomaly detection model."""
        self.model.fit(data)

    def detect_anomalies(self, data):
        """Detect anomalies in the given data."""
        predictions = self.model.predict(data)
        return predictions

if __name__ == "__main__":
    # Example data: 2D points
    data = np.array([[1, 2], [1, 2.5], [1, 3], [10, 10]])
    security_ai = SecurityAI()
    security_ai.train(data)
    anomalies = security_ai.detect_anomalies(data)
    print("Anomaly Detection Results:", anomalies)
