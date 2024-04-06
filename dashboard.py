# Import required modules and libraries
import os
import nbformat
import streamlit as st
from io import BytesIO
import base64

# Function to read and process notebook content
def process_notebook_content(notebook_content: str) -> list:
    """Read and process notebook content.

    Args:
        notebook_content (str): Contents of the notebook.

    Returns:
        list: List of processed outputs.
    """
    outputs = []

    try:
        notebook = nbformat.reads(notebook_content, as_version=4)

        for cell in notebook.cells:
            if cell.cell_type == "code" and cell.get("outputs", []):
                for output in cell.outputs:
                    if output.output_type == "display_data":
                        if "data" in output and "text/html" in output.data:
                            outputs.append(output.data["text/html"])
                        elif "data" in output and "image/png" in output.data:
                            image_data = output.data["image/png"]
                            image_html = f'<img src="data:image/png;base64,{image_data}" />\n'
                            outputs.append(image_html)
                    elif output.output_type == "execute_result":
                        if "data" in output and "text/plain" in output.data:
                            output_text = output.data["text/plain"]
                            outputs.append(f"<pre>{output_text}</pre>")
    except Exception as e:
        st.error(f"An error occurred: {e}")

    return outputs

# Function to display data analysis outputs
def display_data_analysis_output(uploaded_file: BytesIO = None) -> None:
    """Display data analysis outputs.

    Args:
        uploaded_file (BytesIO, optional): Uploaded notebook file. Defaults to None.

    Returns:
        None
    """
    if uploaded_file:
        notebook_content = uploaded_file.getvalue().decode("utf-8")
    else:
        with open("notebooks/05_data_analysis.ipynb", "r", encoding="utf-8") as f:
            notebook_content = f.read()
    outputs = process_notebook_content(notebook_content)

    if outputs:
        for output in outputs:
            st.markdown(output, unsafe_allow_html=True)
    else:
        st.write("No analysis outputs to display.")

# Function to display data visualisation outputs with spacing in between
def display_data_visualisation_output(uploaded_file: BytesIO = None) -> None:
    """Display data visualisation outputs with spacing in between.

    Args:
        uploaded_file (BytesIO, optional): Uploaded notebook file. Defaults to None.

    Returns:
        None
    """
    if uploaded_file:
        notebook_content = uploaded_file.getvalue().decode("utf-8")
    else:
        with open("notebooks/06_data_visualisation.ipynb", "r", encoding="utf-8") as f:
            notebook_content = f.read()
    outputs = process_notebook_content(notebook_content)

    if outputs:
        for output in outputs:
            st.markdown(output, unsafe_allow_html=True)
            st.write("---")
    else:
        st.write("No visualisation outputs to display.")

# Function to download HTML file containing outputs
def download_outputs_html(uploaded_file: BytesIO = None) -> None:
    """Save HTML file containing outputs to downloaded data directory.

    Args:
        uploaded_file (BytesIO, optional): Uploaded notebook file. Defaults to None.

    Returns:
        None
    """
    if uploaded_file:
        notebook_content = uploaded_file.getvalue().decode("utf-8")
    else:
        if st.session_state.page == "Data Analysis":
            with open("notebooks/05_data_analysis.ipynb", "r", encoding="utf-8") as f:
                notebook_content = f.read()
            file_name = "outputs_analysis.html"
        elif st.session_state.page == "Data Visualisation":
            with open("notebooks/06_data_visualisation.ipynb", "r", encoding="utf-8") as f:
                notebook_content = f.read()
            file_name = "outputs_visualisation.html"
    outputs = process_notebook_content(notebook_content)

    # Ensure directory for downloaded data exists
    download_directory = "downloaded_data"
    os.makedirs(download_directory, exist_ok=True)

    # Create HTML content
    html_content = ""
    for output in outputs:
        html_content += output + "\n<hr>\n"
    
    # Save the file
    file_path = os.path.join(download_directory, file_name)
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(html_content)
    
    st.success(f"File saved in {file_path}")

# Set up Streamlit dashboard with page navigation
def main():
    st.title("GitHub Data Analysis Dashboard")

    # Sidebar options
    st.session_state.page = st.sidebar.selectbox("Select a page", ["Data Analysis", "Data Visualisation"])

    # If data analysis selected
    if st.session_state.page == "Data Analysis":
        st.header("Data Analysis Outputs")

        # Allow user to upload a notebook for data analysis
        uploaded_file = st.file_uploader("Upload a notebook for Data Analysis", type=["ipynb"])
        display_data_analysis_output(uploaded_file)

    # If data visualisation selected
    elif st.session_state.page == "Data Visualisation":
        st.header("Data Visualisation Outputs")

        # Allow user to upload a notebook for data visualisation
        uploaded_file = st.file_uploader("Upload a notebook for Data Visualisation", type=["ipynb"])
        display_data_visualisation_output(uploaded_file)

    # Download outputs
    if st.button("Generate HTML File of Outputs"):
        download_outputs_html(uploaded_file)

# Check if script is being run directly, as the main program
# If so, call the main() function to set up and run Streamlit dashboard
if __name__ == "__main__":
    main()
