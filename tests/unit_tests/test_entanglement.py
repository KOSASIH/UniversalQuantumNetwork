import unittest
from src.quantum_comm.entanglement import EntanglementProtocol

class TestEntanglementProtocol(unittest.TestCase):
    def setUp(self):
        self.protocol = EntanglementProtocol()

    def test_entangled_state(self):
        state = self.protocol.entangled_state()
        self.assertEqual(len(state), 4)  # Expecting a 2-qubit entangled state

if __name__ == "__main__":
    unittest.main()
