#!/bin/bash

# Exit on error
set -e

echo "Creating virtual environment..."
python3 -m venv .venv --system-site-packages

# Activate the virtual environment
source .venv/bin/activate

echo "Updating pip and installing build dependencies..."
pip install --upgrade pip
pip install hatchling

echo "Installing project in editable mode..."
# This will install 'click' and map the 'ssh-tools' command
pip install -e .

echo "--------------------------------------"
echo "Setup complete!"
echo "Run 'source .venv/bin/activate' to start."
echo "Then try: ssh-tools --version"