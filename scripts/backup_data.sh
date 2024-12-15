#!/bin/bash

# Script for backing up data for the Universal Quantum Network (UQN)

echo "Backing up data..."

# Define backup directory
BACKUP_DIR="backup_$(date +%Y%m%d_%H%M%S)"
mkdir -p $BACKUP_DIR

# Copy data files to the backup directory
cp -r data/* $BACKUP_DIR/

echo "Backup completed successfully. Backup stored in $BACKUP_DIR."
