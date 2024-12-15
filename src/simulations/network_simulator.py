import numpy as np

class NetworkSimulator:
    def __init__(self, topology):
        self.topology = topology  # Adjacency matrix representing the network

    def simulate_traffic(self, source, destination, traffic_load):
        """Simulate network traffic from source to destination."""
        # Simplified simulation: assume traffic is evenly distributed
        path_length = self.find_path_length(source, destination)
        if path_length > 0:
            return traffic_load / path_length
        else:
            return 0  # No path found

    def find_path_length(self, source, destination):
        """Find the length of the path between source and destination."""
        # For simplicity, return a fixed path length
        return np.random.randint(1, 5)  # Random path length for simulation

if __name__ == "__main__":
    topology = np.array([[0, 1, 0, 1],
                         [1, 0, 1, 0],
                         [0, 1, 0, 1],
                         [1, 0, 1, 0]])
    simulator = NetworkSimulator(topology)
    traffic = simulator.simulate_traffic(0, 3, traffic_load=100)
    print("Simulated Traffic Load:", traffic)
