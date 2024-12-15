from src.quantum_comm.entanglement import EntanglementProtocol

def main():
    # Demo for entanglement communication
    protocol = EntanglementProtocol()
    entangled_state = protocol.entangled_state()
    print("Demo Entanglement: Entangled State:", entangled_state)

if __name__ == "__main__":
    main()
