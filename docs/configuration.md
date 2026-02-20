# ⚙️ Configuration Guide

[cite_start]DocuGenius uses the `pyproject.toml` file to standardize documentation rules across your project[cite: 11, 32].

### **Project Settings**
Add the following section to your `pyproject.toml` to customize the behavior of the validator:

```toml
[tool.docstring_generator]
# Set the documentation style (numpy, google, or pep257)
convention = "numpy"

# Set your target documentation coverage percentage
min_coverage = 90

# Define which files to include in the audit
match = "(?!tests/).*\\.py"