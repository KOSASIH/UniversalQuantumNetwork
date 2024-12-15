class CongestionControl:
    def __init__(self):
        self.congestion_level = 0  # 0: No congestion, 1: Low, 2: Medium, 3: High

    def detect_congestion(self, traffic):
        """Detect congestion based on traffic levels."""
        if traffic > 80:
            self.congestion_level = 3  # High congestion
        elif traffic > 50:
            self.congestion_level = 2  # Medium congestion
        elif traffic > 20:
            self.congestion_level = 1  # Low congestion
        else:
            self.congestion_level = 0  # No congestion

    def take_action(self):
        """Take action based on congestion level."""
        if self.congestion_level == 3:
            print("High congestion detected! Reducing data transmission rate.")
        elif self.congestion_level == 2:
            print("Medium congestion detected! Monitoring traffic.")
        elif self.congestion_level == 1:
            print("Low congestion detected. Normal operation.")
        else:
            print("No congestion detected. All systems normal.")

if __name__ == "__main__":
    congestion_control = CongestionControl()
    congestion_control.detect_congestion(85)  # Example traffic level
    congestion_control.take_action()
