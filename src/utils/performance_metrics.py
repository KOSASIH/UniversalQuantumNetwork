import numpy as np

class PerformanceMetrics:
    @staticmethod
    def calculate_accuracy(true_labels, predicted_labels):
        """Calculate accuracy of predictions."""
        return np.mean(np.array(true_labels) == np.array(predicted_labels))

    @staticmethod
    def calculate_precision(true_labels, predicted_labels):
        """Calculate precision of predictions."""
        true_positive = np.sum((np.array(predicted_labels) == 1) & (np.array(true_labels) == 1))
        false_positive = np.sum((np.array(predicted_labels) == 1) & (np.array(true_labels) == 0))
        return true_positive / (true_positive + false_positive) if (true_positive + false_positive) > 0 else 0

if __name__ == "__main__":
    true_labels = [1, 0, 1, 1, 0]
    predicted_labels = [1, 0, 1, 0, 1]
    accuracy = PerformanceMetrics.calculate_accuracy(true_labels, predicted_labels)
    precision = PerformanceMetrics.calculate_precision(true_labels, predicted_labels)
    print("Accuracy:", accuracy)
    print("Precision:", precision)
