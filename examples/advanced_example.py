from src.ai_integration.ai_optimizer import AIOptimizer
from src.network_protocols.routing import RoutingAlgorithm
import numpy as np

def main():
    # Advanced example of AI optimization
    def objective_function(x):
        return (x - 3) ** 2

    optimizer = AIOptimizer(objective_function)
    optimal_value = optimizer.optimize(initial_guess=[0])
    print("Advanced Example: Optimal Value:", optimal_value)

    # Advanced example of routing algorithm
    topology = np.array([[0, 1, 4, 0],
                         [1, 0, 2, 5],
                         [4, 2, 0, 1],
                         [0, 5, 1, 0]])
    routing = RoutingAlgorithm(topology)
    shortest_path_distance = routing.dijkstra(0, 3)
    print("Advanced Example: Shortest Path Distance from Node 0 to Node 3:", shortest_path_distance)

if __name__ == "__main__":
    main()
