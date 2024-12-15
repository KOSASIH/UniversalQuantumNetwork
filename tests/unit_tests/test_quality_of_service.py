import unittest
from src.network_protocols.quality_of_service import QualityOfService

class TestQualityOfService(unittest.TestCase):
    def setUp(self):
        self.qos = QualityOfService()

    def test_set_qos(self):
        self.qos.set_qos("bandwidth", "100Mbps")
        self.assertEqual(self.qos.get_qos()["bandwidth"], "100Mbps")

if __name__ == "__main__":
    unittest.main()
