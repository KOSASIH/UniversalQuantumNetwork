import numpy as np

class RoutingAlgorithm:
    def __init__(self, topology):
        self.topology = topology  # Adjacency matrix representing the network

    def dijkstra(self, start, end):
        """Implement Dijkstra's algorithm for shortest path routing."""
        num_nodes = len(self.topology)
        visited = [False] * num_nodes
        distances = [float('inf')] * num_nodes
        distances[start] = 0

        for _ in range(num_nodes):
            min_distance = float('inf')
            min_index = -1
            for v in range(num_nodes):
                if not visited[v] and distances[v] < min_distance:
                    min_distance = distances[v]
                    min_index = v

            visited[min_index] = True

            for v in range(num_nodes):
                if (self.topology[min_index][v] > 0 and
                        not visited[v] and
                        distances[min_index] + self.topology[min_index][v] < distances[v]):
                    distances[v] = distances[min_index] + self.topology[min_index][v]

        return distances[end]

if __name__ == "__main__":
    # Example topology (adjacency matrix)
    topology = np.array([[0, 1, 4, 0],
                         [1, 0, 2, 5],
                         [4, 2, 0, 1],
                         [0, 5, 1, 0]])
    routing = RoutingAlgorithm(topology)
    shortest_path_distance = routing.dijkstra(0, 3)
    print("Shortest Path Distance from Node 0 to Node 3:", shortest_path_distance)
