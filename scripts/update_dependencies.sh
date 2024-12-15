#!/bin/bash

# Script to update project dependencies for the Universal Quantum Network (UQN)

echo "Updating project dependencies..."

# Activate the virtual environment
source venv/bin/activate

# Update pip
pip install --upgrade pip

# Update all dependencies
pip install -r requirements.txt --upgrade

echo "Dependencies updated successfully."
