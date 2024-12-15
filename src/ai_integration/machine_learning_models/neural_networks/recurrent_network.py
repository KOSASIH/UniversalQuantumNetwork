import tensorflow as tf
from tensorflow.keras import layers, models

class RecurrentNetwork:
    def __init__(self):
        self.model = models.Sequential([
            layers.SimpleRNN(50, input_shape=(10, 1)),
            layers.Dense(1)
        ])

    def compile_model(self):
        """Compile the RNN model."""
        self.model.compile(optimizer='adam', loss='mean_squared_error')

if __name__ == "__main__":
    rnn = RecurrentNetwork()
    rnn.compile_model()
    print("Recurrent Network Compiled.")
