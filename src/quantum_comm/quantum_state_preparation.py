import numpy as np
from qiskit import QuantumCircuit, Aer, execute

class QuantumStatePreparation:
    def __init__(self):
        self.backend = Aer.get_backend('statevector_simulator')

    def prepare_state(self, state_vector):
        """Prepare a quantum state from a given state vector."""
        circuit = QuantumCircuit(len(state_vector))
        circuit.initialize(state_vector, range(len(state_vector)))
        return circuit

    def simulate(self, circuit):
        """Simulate the quantum circuit and return the state vector."""
        job = execute(circuit, self.backend)
        result = job.result()
        statevector = result.get_statevector()
        return statevector

if __name__ == "__main__":
    state_vector = [1/np.sqrt(2), 1/np.sqrt(2)]  # |+> state
    state_preparation = QuantumStatePreparation()
    circuit = state_preparation.prepare_state(state_vector)
    statevector = state_preparation.simulate(circuit)
    print("Prepared State:", statevector)
