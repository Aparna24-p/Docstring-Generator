"""Main application for AI Docstring Generator - Milestone 4 Final Version."""
import streamlit as st
import toml
import subprocess
import os
import ast
import pandas as pd

# --- 1. SETTINGS LOADER ---
def load_project_settings():
    """
    Load project configuration from the pyproject.toml file.

    Returns
    -------
    tuple
        A string representing the docstring style and an integer for the threshold.
    """ 
    try:
        config = toml.load("pyproject.toml")
        settings = config.get('tool', {}).get('docstring-generator', {})
        style = settings.get('style', 'numpy')
        threshold = settings.get('coverage_threshold', 90)
        return style, threshold
    except Exception:
        return "numpy", 90

# --- 2. CORE LOGIC ---
def collect_coverage(file_path):
    """
    Analyze a Python file to determine docstring coverage and detect edge cases.

    Parameters
    ----------
    file_path : str
        The path to the Python file to be analyzed.

    Returns
    -------
    dict or tuple
        Coverage statistics or a syntax error indicator.
    """
    try:
        with open(file_path, "r") as f:
            content = f.read()
            if not content.strip(): 
                return {'total': 0, 'documented': 0, 'perc': 100, 'details': []}
            tree = ast.parse(content)
        details = []
        for node in ast.walk(tree): 
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
                node_type = "Class" if isinstance(node, ast.ClassDef) else "Function"
                has_doc = ast.get_docstring(node) is not None
                details.append({"Type": node_type, "Name": node.name, "Status": "✅ Documented" if has_doc else "❌ Undocumented"})
        total = len(details)
        documented = sum(1 for item in details if "✅" in item["Status"])
        perc = (documented / total * 100) if total > 0 else 100
        return {'total': total, 'documented': documented, 'perc': perc, 'details': details}
    except Exception as e:
        return "SYNTAX_ERROR", str(e)

# --- 3. MAIN UI WRAPPER ---
def main():
    """
    Initialize and run the Streamlit web interface for the Docstring tool.

    This function handles the sidebar configuration, file uploads, and 
    renders the final coverage and compliance reports.
    """
    st.set_page_config(page_title="DocstringUI Pro", layout="wide")
    config_style, config_threshold = load_project_settings()

    # SIDEBAR
    with st.sidebar:
        st.header("⚙️ Configuration")
        st.info(f"TOML Target: {config_style.upper()}", icon="🎯")
        st.caption("Default style from pyproject.toml")
        st.info(f"TOML Threshold: {config_threshold}%", icon="📊")
        st.caption("Minimum required coverage")
        st.divider()
        ui_style = st.selectbox("Override Docstring Style", ["numpy", "google", "reST"])
        with st.expander("📚 Help: What is a Docstring?"):
            st.write("A string literal used to document Python code. It is the first statement in a function or class.")

    st.title("🚀 AI Docstring Generator & Validator")
    st.write("Ensuring standardized formats and automated quality checks.")

    uploaded_file = st.file_uploader("Upload Python script", type=['py'])

    if uploaded_file:
        path = "temp_upload.py"
        with open(path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        stats = collect_coverage(path)
        
        if isinstance(stats, tuple) and stats[0] == "SYNTAX_ERROR":
            st.error("❌ Syntax Error: The tool cannot process broken Python code.")
            return

        # --- COMPONENT ANALYSIS ---
        st.header("📊 Component Analysis")
        search_query = st.text_input("🔍 Search functions or classes by name", placeholder="Type to filter...")
        
        if stats['details']:
            df = pd.DataFrame(stats['details'])
            if search_query:
                df = df[df['Name'].str.contains(search_query, case=False)]
            st.table(df)
        else:
            st.info("No components found in this file.")

        # --- UPDATED FINAL REPORT SECTION ---
        st.divider()
        st.header("Final Coverage & Compliance Report")
        
        # Row 1: Metrics in one line
        c1, c2, c3 = st.columns(3)
        c1.metric("Total Items", stats['total'])
        c2.metric("Documentation Coverage", f"{stats['perc']:.2f}%")
        
        if stats['total'] == 0:
            c3.metric("Compliance Status", "PASSED (100%)")
            st.success("✅ The code is now fully compliant with PEP 257 and selected standards.")
        else:
            # Show status with percentage
            final_status = "PASSED" if stats['perc'] >= config_threshold else "FAILED"
            c3.metric("Compliance Status", f"{final_status} ({stats['perc']:.0f}%)")
            
            if final_status == "PASSED":
                st.success(f"✅ The code is now fully compliant with PEP 257 and {ui_style.upper()} standards.")
            else:
                st.warning(f"⚠️ Code does not yet meet the {config_threshold}% threshold.")

if __name__ == "__main__":
    main()