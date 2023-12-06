library(reticulate)

# Specify the paths to your Python scripts
py_software <- "software.py"
py_barcodes <- "barcodes.py"
py_backtrack <- "backtrack.py"

# Source the Python scripts in R
source_python(py_software)
source_python(py_barcodes)
source_python(py_backtrack)

# Example of calling Python functions from R
# Replace these function calls with your own logic

# Call functions from software.py
result_software <- py$your_function_from_software_py()

# Call functions from barcodes.py
result_barcodes <- py$your_function_from_barcodes_py()

# Call functions from backtrack.py
result_backtrack <- py$your_function_from_backtrack_py()

# Display results obtained from Python
print(result_software)
print(result_barcodes)
print(result_backtrack)
