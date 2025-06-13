#!/bin/bash
# Exit on any error
set -e

echo "Virtual environment not active. Activating it..."
# Check if Unix-style path exists, else try Windows path.
if [ -f "venv/bin/activate" ]; then
    source venv/bin/activate
elif [ -f "venv/Scripts/activate" ]; then
    source venv/Scripts/activate
else
    echo "Error: Cannot find virtual environment activation script."
    exit 1
fi

# Now that the virtual environment is active, run Python analysis script.
python league_analysis.py
