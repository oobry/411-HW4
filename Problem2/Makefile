# Variables
PYTHON = python3
SCRIPT = topological_sort.py

# Default target: Run the script
run:
	$(PYTHON) $(SCRIPT)

# Check for syntax errors
lint:
	flake8 $(SCRIPT)

# Clean up (if needed)
clean:
	rm -f *.pyc __pycache__/*
