import numpy as np
from qiskit import QuantumCircuit, Aer, execute

class QuantumErrorCorrection:
    def __init__(self):
        self.backend = Aer.get_backend('qasm_simulator')

    def encode(self, state):
        """Encode a qubit into a three-qubit code."""
        circuit = QuantumCircuit(3)
        circuit.initialize(state, 0)
        circuit.cx(0, 1)
        circuit.cx(0, 2)
        return circuit

    def decode(self, circuit):
        """Decode the three-qubit code back to a single qubit."""
        circuit.cx(1, 0)
        circuit.cx(2, 0)
        return circuit

    def simulate(self, circuit):
        """Simulate the quantum circuit and return the result."""
        job = execute(circuit, self.backend)
        result = job.result()
        counts = result.get_counts()
        return counts

if __name__ == "__main__":
    state_to_encode = [1, 0]  # |0> state
    error_correction = QuantumErrorCorrection()
    circuit = error_correction.encode(state_to_encode)
    circuit = error_correction.decode(circuit)
    result = error_correction.simulate(circuit)
    print("Error Correction Result:", result)
