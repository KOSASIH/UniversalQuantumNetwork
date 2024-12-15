import numpy as np
from qiskit import QuantumCircuit, Aer, execute

class EntanglementProtocol:
    def __init__(self):
        self.backend = Aer.get_backend('statevector_simulator')

    def create_entangled_pair(self):
        """Create an entangled pair of qubits using a Bell state."""
        circuit = QuantumCircuit(2)
        circuit.h(0)  # Apply Hadamard gate to the first qubit
        circuit.cx(0, 1)  # Apply CNOT gate to create entanglement
        return circuit

    def simulate(self, circuit):
        """Simulate the quantum circuit and return the state vector."""
        job = execute(circuit, self.backend)
        result = job.result()
        statevector = result.get_statevector()
        return statevector

    def entangled_state(self):
        """Generate and return the entangled state."""
        circuit = self.create_entangled_pair()
        statevector = self.simulate(circuit)
        return statevector

if __name__ == "__main__":
    protocol = EntanglementProtocol()
    entangled_state = protocol.entangled_state()
    print("Entangled State:", entangled_state)
