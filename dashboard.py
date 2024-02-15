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

# Function to display data analysis outputs
def display_data_analysis_output():
    output_html = process_notebook_content("notebooks/05_data_analysis.ipynb")

    st.write("Data analysis outputs:")
    for output in output_html:
        st.markdown(output, unsafe_allow_html=True)

# Function to display data visualisation outputs
def display_data_visualisation_output():
    output_html = process_notebook_content("notebooks/06_data_visualisation.ipynb")

    st.write("Data visualisation outputs:")
    for output in output_html:
        st.markdown(output, unsafe_allow_html=True)

# Set up Streamlit dashboard with page navigation
def main():
    st.title("GitHub Data Analysis Dashboard")

    # Sidebar options
    page = st.sidebar.selectbox("Select a page", ["Data Analysis", "Data Visualisation"])

    # Data analysis content
    if page == "Data Analysis":
        st.header("Data Analysis Page")
        display_data_analysis_output()

    # Data visualisation content
    elif page == "Data Visualisation":
        st.header("Data Visualisation Page")
        display_data_visualisation_output()

# Check if script is being run directly, as the main program
# If so, call the main() function to set up and run Streamlit dashboard
if __name__ == "__main__":
    main()
