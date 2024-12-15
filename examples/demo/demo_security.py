from src.security.intrusion_detection import IntrusionDetectionSystem

def main():
    # Demo for security features
    ids = IntrusionDetectionSystem()
    traffic_data = [0.5, 0.7, 0.9, 0.2, 0.1]  # Simulated traffic data
    for data in traffic_data:
        ids.detect_intrusion(data)

if __name__ == "__main__":
    main()
