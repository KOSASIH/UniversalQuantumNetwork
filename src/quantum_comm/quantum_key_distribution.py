import numpy as np
from qiskit import QuantumCircuit, Aer, execute

class QuantumKeyDistribution:
    def __init__(self):
        self.backend = Aer.get_backend('qasm_simulator')

    def bb84_protocol(self):
        """Implement the BB84 quantum key distribution protocol."""
        circuit = QuantumCircuit(2, 2)
        circuit.h(0)  # Prepare qubit in superposition
        circuit.measure(0, 0)  # Measure the qubit
        return circuit

    def simulate(self, circuit):
        """Simulate the quantum circuit and return the result."""
        job = execute(circuit, self.backend)
        result = job.result()
        counts = result.get_counts()
        return counts

if __name__ == "__main__":
    qkd = QuantumKeyDistribution()
    circuit = qkd.bb84_protocol()
    result = qkd.simulate(circuit)
    print("QKD Result:", result)
