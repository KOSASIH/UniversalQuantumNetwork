import tensorflow as tf
from tensorflow.keras import layers, models

class TransformerModel:
    def __init__(self, input_shape):
        self.model = models.Sequential([
            layers.Input(shape=input_shape),
            layers.MultiHeadAttention(num_heads=2, key_dim=2),
            layers.GlobalAveragePooling1D(),
            layers.Dense(10, activation='softmax')
        ])

    def compile_model(self):
        """Compile the Transformer model."""
        self.model.compile (optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

if __name__ == "__main__":
    input_shape = (None, 64)  # Example input shape
    transformer = TransformerModel(input_shape)
    transformer.compile_model()
    print("Transformer Model Compiled.")
