#!/bin/bash

# Check if we're in a virtual environment
if [ -z "$VIRTUAL_ENV" ]; then
    echo "Virtual environment not active. Activating it..."
    source venv/bin/activate
else
    echo "Virtual environment is already active."
fi

# Run the analysis script
python3 ./league_analysis.py
