import numpy as np
from scipy.optimize import minimize

class AIOptimizer:
    def __init__(self, objective_function):
        self.objective_function = objective_function

    def optimize(self, initial_guess):
        """Optimize the given objective function."""
        result = minimize(self.objective_function, initial_guess)
        return result

if __name__ == "__main__":
    # Example objective function: f(x) = (x - 3)^2
    def objective_function(x):
        return (x - 3) ** 2

    optimizer = AIOptimizer(objective_function)
    optimal_value = optimizer.optimize(initial_guess=[0])
    print("Optimal Value:", optimal_value)
