import numpy as np
from qiskit import QuantumCircuit, Aer, execute

class SuperpositionProtocol:
    def __init__(self):
        self.backend = Aer.get_backend('statevector_simulator')

    def create_superposition(self):
        """Create a superposition state using a Hadamard gate."""
        circuit = QuantumCircuit(1)
        circuit.h(0)  # Apply Hadamard gate to create superposition
        return circuit

    def simulate(self, circuit):
        """Simulate the quantum circuit and return the state vector."""
        job = execute(circuit, self.backend)
        result = job.result()
        statevector = result.get_statevector()
        return statevector

if __name__ == "__main__":
    protocol = SuperpositionProtocol()
    superposition_circuit = protocol.create_superposition()
    statevector = protocol.simulate(superposition_circuit)
    print("Superposition State:", statevector)
