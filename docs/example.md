# 📖 Quick Start Example

This guide walks you through a typical session using the DocuGenius platform to audit and improve your code documentation.

### **Step 1: Preparing Your File**
Start with a standard Python script that needs better documentation, such as a file with simple one-line docstrings or missing parameters.

### **Step 2: Uploading to the Dashboard**
1. Launch the UI using `streamlit run src/docstring_generator/app.py`.
2. Click the **Browse files** button and select your Python script.

### **Step 3: Analyzing Compliance**
- **Documentation Coverage**: Check the gauge chart to see your current quality score.
- **Component Search**: Use the search bar to instantly find specific functions like `calculate_average`.

### **Step 4: Reviewing Audit Results**
Scroll down to the **PEP-257 Violations** section. Here, the tool will list specific issues:
* **Error Codes**: Identify exactly what is wrong (e.g., **D407** for missing underlines).
* **Line Numbers**: Find the exact line in your code that needs attention.

### **Step 5: Implementation**
Update your docstrings to meet the **NumPy-style** standards shown in the **API Reference** section of these docs. Once updated, re-upload the file to see your coverage reach **100%!**.