import streamlit as st
import sqlite3
import os
import tempfile
from compare_function import compare_file  # Import your compare_file function here

# Function to create database table for users
def create_table():
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users
                 (username TEXT PRIMARY KEY, password TEXT)''')
    conn.commit()
    conn.close()

# Function to insert new user into database
def insert_user(username, password):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
    conn.commit()
    conn.close()

# Function to check if username exists in database
def username_exists(username):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE username=?", (username,))
    result = c.fetchone()
    conn.close()
    return result is not None

# Function to verify login credentials
def verify_login(username, password):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    result = c.fetchone()
    conn.close()
    return result is not None

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

    # Create database table if not exists
    create_table()

    # Sidebar for register and login
    st.sidebar.title("User Authentication")
    username = st.sidebar.text_input("Username")
    password = st.sidebar.text_input("Password", type="password")

    # Registration
    if st.sidebar.button("Register"):
        if username == "" or password == "":
            st.warning("Please enter both username and password.")
        elif username_exists(username):
            st.warning("Username already exists. Please choose a different username.")
        else:
            insert_user(username, password)
            st.success("Registration successful. You can now login.")

    # Login
    login_button = st.sidebar.button("Login")
    if login_button:
        if verify_login(username, password):
            st.sidebar.success(f"Welcome, {username}!")
        else:
            st.sidebar.error("Invalid username or password. Please try again.")

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