import unittest
from src.network_protocols.network_simulator import NetworkSimulator
import numpy as np

class TestNetworkSimulator(unittest.TestCase):
    def setUp(self):
        self.topology = np.array([[0, 1, 0, 1],
                                  [1, 0, 1, 0],
                                  [0, 1, 0, 1],
                                  [1, 0, 1, 0]])
        self.simulator = NetworkSimulator(self.topology)

    def test_network_functionality(self):
        performance_metrics = self.simulator.evaluate_performance()
        self.assertIn('latency', performance_metrics)  # Check if latency is part of metrics

if __name__ == "__main__":
    unittest.main()
