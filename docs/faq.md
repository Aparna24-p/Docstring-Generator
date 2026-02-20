# ❓ Troubleshooting & FAQ

Common questions and solutions for using DocuGenius.

### **General Questions**

**Q: Why is my Documentation Coverage score 0%?**
**A:** This usually happens if your Python file contains no functions or classes, or if they are entirely empty. Ensure your code has at least one defined component for the AST parser to detect.

**Q: Does the tool support Google or reStructuredText styles?**
**A:** While Milestone 4 focuses on **NumPy-style** compliance, the underlying architecture is designed to be multi-format. You can toggle conventions in your `pyproject.toml`.

### **Technical Troubleshooting**

**Q: I see a Red Error box when I upload a file. What does it mean?**
**A:** This indicates a **Syntax Error** in the uploaded Python file. The tool cannot audit code that cannot be parsed by the Python interpreter. Fix the code and try uploading again.

**Q: What do error codes like D103 or D407 mean?**
**A:** These are standard **PEP-257 violation codes**. 
- **D103**: Missing docstring in a public function.
- **D407**: Missing dashed underline after a section (e.g., Parameters).

**Q: How do I exclude my `tests/` folder from being scanned?**
**A:** Add the `match = "(?!tests/).*\\.py"` rule to your `pyproject.toml` under the `[tool.pydocstyle]` section.