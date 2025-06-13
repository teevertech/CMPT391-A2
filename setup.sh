#!/bin/bash

# Exit on any error
set -e

# Create virtual environment
python3 -m venv venv

# Activate the virtual environment
if [ -f "venv/bin/activate" ]; then
    source venv/bin/activate
elif [ -f "venv/Scripts/activate" ]; then
    source venv/Scripts/activate
else
    echo "Could not find activation script."
    exit 1
fi

# Upgrade pip and install dependencies
pip install --upgrade pip
pip install pandas
pip install scikit-learn
pip install matplotlib
pip install mlxtend

# Freeze dependencies
pip freeze > requirements.txt

chmod +x ./run.sh
chmod +x ./league_analysis.py

echo "Virtual environment setup complete. Activate it with: ./run.sh"
