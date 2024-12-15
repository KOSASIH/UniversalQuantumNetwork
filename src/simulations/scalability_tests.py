import time

class ScalabilityTests:
    def __init__(self):
        self.results = []

    def test_scalability(self, num_nodes):
        """Test the scalability of the network with a given number of nodes."""
        start_time = time.time()
        # Simulate some processing for scalability
        time.sleep(num_nodes * 0.1)  # Simulated processing time
        end_time = time.time()
        execution_time = end time - start_time
        self.results.append((num_nodes, execution_time))
        print(f"Scalability test with {num_nodes} nodes took {execution_time:.4f} seconds.")

if __name__ == "__main__":
    scalability_test = ScalabilityTests()
    for nodes in range(1, 6):  # Testing scalability from 1 to 5 nodes
        scalability_test.test_scalability(nodes)
