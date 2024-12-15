class CrossLayerOptimization:
    def __init__(self):
        self.optimization_parameters ```python
= {}

    def set_parameter(self, layer, parameter, value):
        """Set an optimization parameter for a specific layer."""
        if layer not in self.optimization_parameters:
            self.optimization_parameters[layer] = {}
        self.optimization_parameters[layer][parameter] = value
        print(f"Parameter '{parameter}' for layer '{layer}' set to {value}.")

    def get_parameters(self):
        """Get all optimization parameters."""
        return self.optimization_parameters

if __name__ == "__main__":
    optimization = CrossLayerOptimization()
    optimization.set_parameter("Network Layer", "Throughput", "1000Mbps")
    optimization.set_parameter("Transport Layer", "Latency", "15ms")
    print("Current Optimization Parameters:", optimization.get_parameters())
