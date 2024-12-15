import numpy as np
from qiskit import QuantumCircuit, Aer, execute

class QuantumMeasurement:
    def __init__(self):
        self.backend = Aer.get_backend('qasm_simulator')

    def measure_qubit(self):
        """Create a circuit to measure a qubit."""
        circuit = QuantumCircuit(1, 1)
        circuit.h(0)  # Prepare in superposition
 ```python
        circuit.measure(0, 0)  # Measure the qubit
        return circuit

    def simulate(self, circuit):
        """Simulate the quantum circuit and return the measurement result."""
        job = execute(circuit, self.backend)
        result = job.result()
        counts = result.get_counts()
        return counts

if __name__ == "__main__":
    measurement = QuantumMeasurement()
    circuit = measurement.measure_qubit()
    result = measurement.simulate(circuit)
    print("Measurement Result:", result)
