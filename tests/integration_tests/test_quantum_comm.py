import unittest
from src.quantum_comm.quantum_network import QuantumNetwork

class TestQuantumNetwork(unittest.TestCase):
    def setUp(self):
        self.network = QuantumNetwork()

    def test_quantum_communication(self):
        result = self.network.send_message("Hello Quantum")
        self.assertEqual(result, "Message sent: Hello Quantum")  # Check message sending

if __name__ == "__main__":
    unittest.main()
