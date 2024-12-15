import tensorflow as tf
from tensorflow.keras import layers, models

class ConvolutionalNetwork:
    def __init__(self):
        self.model = models.Sequential([
            layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
            layers.MaxPooling2D((2, 2)),
            layers.Conv2D(64, (3, 3), activation='relu'),
            layers.MaxPooling2D((2, 2)),
            layers.Flatten(),
            layers.Dense(64, activation='relu'),
            layers.Dense(10, activation='softmax')
        ])

    def compile_model(self):
        """Compile the CNN model."""
        self.model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

if __name__ == "__main__":
    cnn = ConvolutionalNetwork()
    cnn.compile_model()
    print("Convolutional Network Compiled.")
