from src.quantum_comm.entanglement import EntanglementProtocol
from src.quantum_comm.teleportation import QuantumTeleportation

def main():
    # Basic example of creating entangled states
    entanglement_protocol = EntanglementProtocol()
    entangled_state = entanglement_protocol.entangled_state()
    print("Basic Example: Entangled State:", entangled_state)

    # Basic example of quantum teleportation
    teleportation_protocol = QuantumTeleportation()
    state_to_teleport = [1, 0]  # |0> state
    teleportation_circuit = teleportation_protocol.teleport(state_to_teleport)
    teleportation_result = teleportation_protocol.simulate(teleportation_circuit)
    print("Basic Example: Teleportation Result:", teleportation_result)

if __name__ == "__main__":
    main()
