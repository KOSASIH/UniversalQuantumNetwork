import unittest
from src.ai_integration.neural_networks.convolutional_network import ConvolutionalNetwork

class TestConvolutionalNetwork(unittest.TestCase):
    def setUp(self):
        self.cnn = ConvolutionalNetwork()
        self.cnn.compile_model()

    def test_model_compilation(self):
        self.assertIsNotNone(self.cnn.model)  # Ensure model is compiled

if __name__ == "__main__":
    unittest.main()
