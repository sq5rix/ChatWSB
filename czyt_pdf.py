import os
import pdfplumber
import re

# Directory containing the PDF files
pdf_directory = '/path/to/pdf/files'

# Regular expression patterns to match specific information
patterns = {
    'data': r'Data: (\d{4}-\d{2}-\d{2})',
    'imię': r'Imię: (\w+)',
    'nazwisko': r'Nazwisko: (\w+)',
    'rok': r'Rok: (\d+)',
    'grupa': r'Grupa: (\w+)',
    'id_studenta': r'Id studenta: (\d+)',
    'temat_pracy': r'Temat pracy: (.*?)\n',
    'domena': r'Domena: (sprzęt/oprogramowanie/dane/kod)',
    'źródła': r'Źródła: (.*?)\n',
    'treść': r'Treść:(.*?)\n\S'
}

def extract_information(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        text = ''
        for page in pdf.pages:
            text += page.extract_text() or ''  # Concatenate text of all pages

        # Dictionary to hold the extracted data
        extracted_data = {}
        
        # Search for each pattern in the text and extract the corresponding information
        for key, pattern in patterns.items():
            match = re.search(pattern, text, re.MULTILINE | re.DOTALL)
            if match:
                extracted_data[key] = match.group(1).strip()

        return extracted_data

# Loop through all PDF files in the directory
for filename in os.listdir(pdf_directory):
    if filename.endswith('.pdf'):
        file_path = os.path.join(pdf_directory, filename)
        info = extract_information(file_path)
        print(f"Information extracted from {filename}: {info}")

