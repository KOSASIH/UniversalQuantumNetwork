import unittest
from src.ai_integration.ai_optimizer import AIOptimizer

class TestAIOptimizer(unittest.TestCase):
    def setUp(self):
        self.optimizer = AIOptimizer(lambda x: (x - 2) ** 2)

    def test_optimize(self):
        optimal_value = self.optimizer.optimize(initial_guess=[0])
        self.assertAlmostEqual(optimal_value.fun, 0, places=2)  # Expecting minimum at x=2

if __name__ == "__main__":
    unittest.main()
