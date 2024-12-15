class NetworkVirtualization:
    def __init__(self):
        self.virtual_networks = {}

    def create_virtual_network(self, network_name):
        """Create a virtual network."""
        if network_name not in self.virtual_networks:
            self.virtual_networks[network_name] = []
            print(f"Virtual network '{network_name}' created.")

    def add_node_to_virtual_network(self, network_name, node):
        """Add a node to a virtual network."""
        if network_name in self.virtual_networks:
            self.virtual_networks[network_name].append(node)
            print(f"Node '{node}' added to virtual network '{network_name}'.")

if __name__ == "__main__":
    virtualization = NetworkVirtualization()
    virtualization.create_virtual_network("Virtual Network 1")
    virtualization.add_node_to_virtual_network("Virtual Network 1", "Node A")
