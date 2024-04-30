import os
import pdfplumber
import re
from db_class import DatabaseAccess

# Directory containing the PDF files
pdf_directory = 'PlikiWejsciowe'

KEYS = [
        'data',
        'imie',
        'nazwisko',
        'rok',
        'grupa',
        'id_studenta',
        'pytanie',
        'tresc',
        'domena',
        'zrodla',
        'tresc',
        ]

# Regular expression patterns to match specific information
patterns = {
    'data': r'Data: (\d{4}-\d{2}-\d{2})',
    'imie': r'Imię: (\w+)',
    'nazwisko': r'Nazwisko: (\w+)',
    'rok': r'Rok: (\d+)',
    'grupa': r'Grupa: (\w+)',
    'id_studenta': r'Id studenta: (\d+)',
    'pytanie': r'Pytanie: (.*?)\n',
    'tresc':  r'Treść odpowiedzi: (.*?)\n',
    'domena': r'Domena: (sprzęt/oprogramowanie/dane/kod)',
    'zrodla': r'Źródła: (.*?)\n',
    'tresc': r'Treść:(.*?)\n\S'
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
        extracted_data['text'] = text
        return extracted_data

def read_all_files():
    all_texts = ""
    for filename in os.listdir(pdf_directory):
        if filename.endswith('.pdf'):
            file_path = os.path.join(pdf_directory, filename)
            info = extract_information(file_path)
            all_texts += info['text']
    return all_texts

if __name__ == "__main__":
    all = read_all_files()
    print(all)
