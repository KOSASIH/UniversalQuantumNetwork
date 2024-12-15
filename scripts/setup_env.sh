#!/bin/bash

# Environment setup script for the Universal Quantum Network (UQN)

echo "Setting up the environment for UQN..."

# Create a virtual environment
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Install required packages
pip install -r requirements.txt

echo "Environment setup completed successfully."
