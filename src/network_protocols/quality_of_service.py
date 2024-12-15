class QualityOfService:
    def __init__(self):
        self.qos_parameters = {}

    def set_qos(self, parameter, value):
        """Set a QoS parameter."""
        self.qos_parameters[parameter] = value
        print(f"QoS parameter '{parameter}' set to {value}.")

    def get_qos(self):
        """Get the current QoS parameters."""
        return self.qos_parameters

if __name__ == "__main__":
    qos = QualityOfService()
    qos.set_qos("bandwidth", "100Mbps")
    qos.set_qos("latency", "20ms")
    print("Current QoS Parameters:", qos.get_qos())
