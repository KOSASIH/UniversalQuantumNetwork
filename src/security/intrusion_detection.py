import numpy as np

class IntrusionDetectionSystem:
    def __init__(self):
        self.threshold = 0.8  # Threshold for anomaly detection

    def detect_intrusion(self, traffic_data):
        """Detect intrusions based on traffic data."""
        # Simulate anomaly detection
        anomaly_score = np.random.rand()  # Random score for simulation
        if anomaly_score > self.threshold:
            print("Intrusion detected! Anomaly score:", anomaly_score)
            return True
        else:
            print("No intrusion detected. Anomaly score:", anomaly_score)
            return False

if __name__ == "__main__":
    ids = IntrusionDetectionSystem()
    traffic_data = np.random.rand(100)  # Simulated traffic data
    ids.detect_intrusion(traffic_data)
