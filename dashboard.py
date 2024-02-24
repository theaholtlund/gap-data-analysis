# Import required modules and libraries
import nbformat
import streamlit as st
from io import BytesIO
import base64

# Function to read and process notebook content
def process_notebook_content(notebook_content):
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
def display_data_analysis_output(uploaded_file):
    notebook_content = uploaded_file.getvalue().decode("utf-8")
    outputs = process_notebook_content(notebook_content)

    if outputs:
        for output in outputs:
            st.markdown(output, unsafe_allow_html=True)
    else:
        st.write("No notebook uploaded. Please upload a notebook for analysis.")

# Function to display data visualisation outputs with spacing in between
def display_data_visualisation_output(uploaded_file):
    notebook_content = uploaded_file.getvalue().decode("utf-8")
    outputs = process_notebook_content(notebook_content)

    if outputs:
        for output in outputs:
            st.markdown(output, unsafe_allow_html=True)
            st.write("---")  # Adding spacing between visualisation outputs
    else:
        st.write("No notebook uploaded. Please upload a notebook for visualisation.")

# Function to download HTML file containing outputs
def download_outputs_html(uploaded_file, combined=False):
    notebook_content = uploaded_file.getvalue().decode("utf-8")
    outputs = process_notebook_content(notebook_content)

    # Create HTML content
    html_content = ""
    for output in outputs:
        html_content += output + "\n<hr>\n"

    # Create HTML file
    with open("outputs.html", "w", encoding="utf-8") as f:
        f.write(html_content)

    # Download HTML file
    with open("outputs.html", "rb") as f:
        b64 = base64.b64encode(f.read()).decode()
        if combined:
            href = f'<a href="data:file/html;base64,{b64}" download="combined_outputs.html">Download Combined Outputs</a>'
        else:
            href = f'<a href="data:file/html;base64,{b64}" download="outputs.html">Download Outputs</a>'
        st.markdown(href, unsafe_allow_html=True)

# Set up Streamlit dashboard with page navigation
def main():
    st.title("GitHub Data Analysis Dashboard")

    # Sidebar options
    page = st.sidebar.selectbox("Select a page", ["Data Analysis", "Data Visualisation"])

    # If data analysis selected
    if page == "Data Analysis":
        st.header("Data Analysis Outputs")
        
        # Allow user to upload a notebook
        uploaded_file = st.file_uploader("Upload a notebook", type=["ipynb"])
        if uploaded_file is not None:
            # Process and display uploaded notebook
            display_data_analysis_output(uploaded_file)
            # Offer download option for analysis outputs
            download_outputs_html(uploaded_file)
        else:
            # Display message when no notebook is uploaded
            st.write("No notebook uploaded. Please upload a notebook for analysis.")

    # If data visualisation selected
    elif page == "Data Visualisation":
        st.header("Data Visualisation Outputs")
        
        # Allow user to upload a notebook
        uploaded_file = st.file_uploader("Upload a notebook", type=["ipynb"])
        if uploaded_file is not None:
            # Process and display uploaded notebook
            display_data_visualisation_output(uploaded_file)
            # Offer download option for visualization outputs
            download_outputs_html(uploaded_file)
        else:
            # Display message when no notebook is uploaded
            st.write("No notebook uploaded. Please upload a notebook for visualisation.")

    # Download both analysis and visualization outputs combined
    if st.button("Download Combined Outputs"):
        if uploaded_file is not None:
            download_outputs_html(uploaded_file, combined=True)
        else:
            st.write("Please upload a notebook first.")

# Check if script is being run directly, as the main program
# If so, call the main() function to set up and run Streamlit dashboard
if __name__ == "__main__":
    main()
