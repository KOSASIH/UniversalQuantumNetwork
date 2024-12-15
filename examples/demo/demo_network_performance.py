from src.network_protocols.network_simulator import NetworkSimulator
import numpy as np

def main():
    # Demo for network performance evaluation
    topology = np.array([[0, 1, 0, 1],
                         [1, 0,1, 0],
                         [0, 1, 0, 1],
                         [1, 0, 1, 0]])
    simulator = NetworkSimulator(topology)
    performance_metrics = simulator.evaluate_performance()
    print("Demo Network Performance: Performance Metrics:", performance_metrics)

if __name__ == "__main__":
    main()
