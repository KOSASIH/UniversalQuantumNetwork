import unittest
from src.security.intrusion_detection import IntrusionDetectionSystem

class TestIntrusionDetection(unittest.TestCase):
    def setUp(self):
        self.ids = IntrusionDetectionSystem()

    def test_detect_intrusion(self):
        result = self.ids.detect_intrusion([0.5, 0.9])
        self.assertIsInstance(result, bool)  # Expecting a boolean result

if __name__ == "__main__":
    unittest.main()
