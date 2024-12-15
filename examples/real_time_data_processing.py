import random
import time

class RealTimeDataProcessor:
    def process_data(self, data):
        """Simulate real-time data processing."""
        print(f"Processing data: {data}")
        time.sleep(1)  # Simulate processing time
        print("Data processed.")

def main():
    processor = RealTimeDataProcessor()
    for _ in range(5):  # Simulate processing 5 data points
        data = random.randint(1, 100)
        processor.process_data(data)

if __name__ == "__main__":
    main()
