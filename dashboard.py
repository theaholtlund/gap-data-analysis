# Import required modules and libraries
import os
import nbformat
import streamlit as st

# Function to read and process notebook content
def process_notebook_content(notebook_path):
    output_html = []

    with open(notebook_path, "r", encoding="utf-8") as f:
        notebook_content = f.read()

    notebook = nbformat.reads(notebook_content, as_version=4)

    for cell in notebook.cells:
        if cell.cell_type == "code" and cell.get("outputs", []):
            for output in cell.outputs:
                if output.output_type == "display_data":
                    if "data" in output and "text/html" in output.data:
                        output_html.append(output.data["text/html"])
                elif output.output_type == "execute_result":
                    if "data" in output and "text/plain" in output.data:
                        output_text = output.data["text/plain"]
                        output_html.append(f"<pre>{output_text}</pre>")
                elif output.output_type == "stream":
                    if "text" in output:
                        output_text = output.text
                        if "Request limit for API Calls:" not in output_text:
                            output_html.append(f"<pre>{output_text}</pre>")

    return output_html

# Function to display outputs of notebook content
def display_data_analysis_output(notebook_path):
    output_html = process_notebook_content(notebook_path)

    st.write("Data analysis outputs:")
    for output in output_html:
        st.markdown(output, unsafe_allow_html=True)

# Set up Streamlit dashboard with page navigation
def main():
    st.title("GitHub Data Analysis Dashboard")

    # Sidebar options
    page = st.sidebar.selectbox("Select a page", ["Overview", "Repositories", "Community"])

    # Content overview
    if page == "Overview":
        st.header("Overview Page")
        # Content overview

    # Repositories content
    elif page == "Repositories":
        st.header("Repositories Page")
        display_data_analysis_output("notebooks/05_data_analysis.ipynb")
        display_data_analysis_output("notebooks/06_data_visualisation.ipynb")

    # Community content
    elif page == "Community":
        st.header("Community Page")

# Check if script is being run directly, as the main program
# If so, call the main() function to set up and run Streamlit dashboard
if __name__ == "__main__":
    main()
