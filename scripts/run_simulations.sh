#!/bin/bash

# Script to run simulations for testing the Universal Quantum Network (UQN)

echo "Running simulations..."

# Activate the virtual environment
source venv/bin/activate

# Run the simulation scripts
python3 src/simulations/quantum_simulator.py
python3 src/simulations/network_simulator.py
python3 src/simulations/scenario_generator.py
python3 src/simulations/fault_tolerance_simulation.py
python3 src/simulations/scalability_tests.py

echo "Simulations completed successfully."
