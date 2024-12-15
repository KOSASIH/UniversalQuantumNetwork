class NetworkTopology:
    def __init__(self):
        self.topology = {}

    def add_node(self, node):
        """Add a node to the network topology."""
        if node not in self.topology:
            self.topology[node] = []

    def add_edge(self, node1, node2):
        """Add an edge between two nodes."""
        if node1 in self.topology and node2 in self.topology:
            self.topology[node1].append(node2)
            self.topology[node2].append(node1)

    def display_topology(self):
        """Display the network topology."""
        for node, edges in self.topology.items():
            print(f"{node}: {edges}")

if __name__ == "__main__":
    network_topology = NetworkTopology()
    network_topology.add_node("Node A")
    network_topology.add_node("Node B")
    network_topology.add_edge("Node A", "Node B")
    network_topology.display_topology()
