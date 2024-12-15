import matplotlib.pyplot as plt

class Visualization:
    @staticmethod
    def plot_data(x, y, title='Data Visualization', xlabel='X-axis', ylabel='Y-axis'):
        """Plot data using Matplotlib."""
        plt.figure(figsize=(10, 5))
        plt.plot(x, y, marker='o')
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.grid()
        plt.show()

if __name__ == "__main__":
    # Example usage
    x = [1, 2, 3, 4, 5]
    y = [2, 3, 5, 7, 11]
    Visualization.plot_data(x, y, title='Example Plot', xlabel='Numbers', ylabel='Prime Numbers')
