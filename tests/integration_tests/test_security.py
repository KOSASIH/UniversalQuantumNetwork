import unittest
from src.security.security_manager import SecurityManager

class TestSecurityManager(unittest.TestCase):
    def setUp(self):
        self.manager = SecurityManager()

    def test_security_features(self):
        result = self.manager.check_security()
        self.assertTrue(result)  # Expecting security checks to pass

if __name__ == "__main__":
    unittest.main()
