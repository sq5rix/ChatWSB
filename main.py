import streamlit as st
import os
import tempfile
from compare_function import compare_file  # Import your compare_file function here

# Function to process uploaded files
def process_files(files):
    report = ""
    for file in files:
        # Check if the file is a PDF
        if file.type == 'application/pdf':
            with st.spinner(f'Processing {file.name}...'):
                # Create a temporary directory to save the PDF file
                with tempfile.TemporaryDirectory() as tmp_dir:
                    filepath = os.path.join(tmp_dir, file.name)
                    with open(filepath, 'wb') as f:
                        f.write(file.getvalue())
                    # Call the compare_file function
                    result = compare_file(filepath)
                    # Append the result to the report
                    report += f"Comparison for {file.name}:\n{result}\n\n"
        else:
            st.warning(f"{file.name} is not a PDF file and will be skipped.")
    return report

# Main application
def main():
    st.title("PDF Comparison Tool")

    # Sidebar for register and login
    st.sidebar.title("User Authentication")
    username = st.sidebar.text_input("Username")
    password = st.sidebar.text_input("Password", type="password")
    login_button = st.sidebar.button("Login")
    if login_button:
        # Placeholder for authentication logic
        st.sidebar.success(f"Welcome, {username}!")

    # Main window
    st.header("Upload PDF Files")
    uploaded_files = st.file_uploader("Upload one or more PDF files", accept_multiple_files=True)

    # Process button
    if st.button("Process"):
        if not uploaded_files:
            st.warning("Please upload at least one PDF file.")
        else:
            # Process the uploaded files
            report = process_files(uploaded_files)
            # Display the report
            st.header("Comparison Report")
            st.text_area("Report", report, height=400)

            # Save report to download
            st.download_button(
                label="Download Report",
                data=report.encode("utf-8"),
                file_name="comparison_report.txt",
                mime="text/plain",
            )

# Run the application
if __name__ == "__main__":
    main()