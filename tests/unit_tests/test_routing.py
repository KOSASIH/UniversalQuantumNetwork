import unittest
import numpy as np
from src.network_protocols.routing import RoutingAlgorithm

class TestRoutingAlgorithm(unittest.TestCase):
    def setUp(self):
        self.topology = np.array([[0, 1, 4, 0],
                                  [1, 0, 2, 5],
                                  [4, 2, 0, 1],
                                  [0, 5, 1, 0]])
        self.routing = RoutingAlgorithm(self.topology)

    def test_dijkstra(self):
        distance = self.routing.dijkstra(0, 3)
        self.assertGreaterEqual(distance, 0)  # Distance should be non-negative

if __name__ == "__main__":
    unittest.main()
