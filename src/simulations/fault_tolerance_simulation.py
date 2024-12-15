class FaultToleranceSimulation:
    def __init__(self):
        self.faults = []

    def introduce_fault(self, fault_type):
        """Introduce a fault into the system."""
        self.faults.append(fault_type)
        print(f"Fault introduced: {fault_type}")

    def simulate_recovery(self):
        """Simulate recovery from faults."""
        if self.faults:
            print("Recovering from faults...")
            self.faults.clear()
            print("Recovery successful.")
        else:
            print("No faults to recover from.")

if __name__ == "__main__":
    simulation = FaultToleranceSimulation()
    simulation.introduce_fault("Quantum Bit Flip")
    simulation.simulate_recovery()
