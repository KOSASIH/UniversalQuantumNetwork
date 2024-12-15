import numpy as np
from qiskit import QuantumCircuit, Aer, execute

class QuantumChannel:
    def __init__(self):
        self.backend = Aer.get_backend('statevector_simulator')

    def apply_noise(self, circuit, noise_type='depolarizing', noise_level=0.1):
        """Apply noise to the quantum channel."""
        if noise_type == 'depolarizing':
            circuit = circuit.depolarizing_error(noise_level)
        return circuit

    def simulate(self, circuit):
        """Simulate the quantum circuit and return the state vector."""
        job = execute(circuit, self.backend)
        result = job.result()
        statevector = result.get_statevector()
        return statevector

if __name__ == "__main__":
    channel = QuantumChannel()
    circuit = QuantumCircuit(1)
    circuit.h(0)  # Create a superposition
    noisy_circuit = channel.apply_noise(circuit)
    statevector = channel.simulate(noisy_circuit)
    print("Noisy State:", statevector)
