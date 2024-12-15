from qiskit import QuantumCircuit, Aer, execute

class QuantumSimulator:
    def __init__(self):
        self.backend = Aer.get_backend('statevector_simulator')

    def run_circuit(self, circuit):
        """Run a quantum circuit and return the state vector."""
        job = execute(circuit, self.backend)
        result = job.result()
        statevector = result.get_statevector()
        return statevector

    def create_sample_circuit(self):
        """Create a sample quantum circuit for demonstration."""
        circuit = QuantumCircuit(2)
        circuit.h(0)  # Apply Hadamard gate to the first qubit
        circuit.cx(0, 1)  # Apply CNOT gate
        return circuit

if __name__ == "__main__":
    simulator = QuantumSimulator()
    sample_circuit = simulator.create_sample_circuit()
    statevector = simulator.run_circuit(sample_circuit)
    print("State Vector:", statevector)
