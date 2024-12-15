import unittest
from src.ai_integration.ai_system import AISystem

class TestAISystem(unittest.TestCase):
    def setUp(self):
        self.ai_system = AISystem()

    def test_ai_integration(self):
        result = self.ai_system.run_integration_test()
        self.assertTrue(result)  # Expecting integration test to pass

if __name__ == "__main__":
    unittest.main()
