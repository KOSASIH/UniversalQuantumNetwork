import numpy as np
from sklearn.linear_model import LinearRegression

class PredictiveModel:
    def __init__(self):
        self.model = LinearRegression()

    def train(self, X, y):
        """Train the predictive model."""
        self.model.fit(X, y)

    def predict(self, X):
        """Make predictions using the trained model."""
        return self.model.predict(X)

if __name__ == "__main__":
    # Example usage
    X = np.array([[1], [2], [3], [4]])
    y = np.array([2, 3, 5, 7])
    predictive_model = PredictiveModel()
    predictive_model.train(X, y)
    predictions = predictive_model.predict(np.array([[5], [6]]))
    print("Predictions:", predictions)
