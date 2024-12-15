import unittest
from src.network_protocols.error_handling import ErrorHandling

class TestErrorHandling(unittest.TestCase):
    def setUp(self):
        self.error_handler = ErrorHandling()

    def test_log_error(self):
        self.error_handler.log_error("Test error")
        self.assertIn("Test error", self.error_handler.error_log)

if __name__ == "__main__":
    unittest.main()
