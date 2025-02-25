# Variables
PYTHON = python3
SCRIPT = DFS.py
INPUT = input.txt
OUTPUT = output.txt

# Default target: Run the script
run: $(SCRIPT) $(INPUT)
	@$(PYTHON) $(SCRIPT) < $(INPUT) > $(OUTPUT)
	@echo "Program executed successfully. Check $(OUTPUT) for results."

# Clean target: Remove generated output files
clean:
	@rm -f $(OUTPUT)
	@echo "Cleaned up output files."
