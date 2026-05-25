#!/bin/bash
set -e
VENV_DIR="venv"
if [ ! -d "$VENV_DIR" ]; then
    echo "ERROR: Virtual environment not found."
    exit 1
fi
echo "Activating virtual environment..."
source "$VENV_DIR/bin/activate"
echo "Running test suite..."
python -m pytest --tb=short -v
TEST_EXIT_CODE=$?
if [ $TEST_EXIT_CODE -eq 0 ]; then
    echo "All tests passed."
else
    echo "One or more tests failed."
fi
exit $TEST_EXIT_CODE
