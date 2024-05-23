import os
import re

from dbclass import Database, Base
from kolokwia import Kolokwia, DB_FILE
from utils import calculate_digest, read_pdf

"""
Przeczytaj wszystkie pliki z folderu pdf_directory
Parsuj i policz digest dla każdego pliku i jeśli
unikalny umieść w tabeli
"""
# Directory containing the PDF files
#pdf_directory = 'PlikiWejsciowe'
pdf_directory = 'PlikiWejsciowe'

# Regular expression patterns to match specific information
patterns = {
    'data': r'Data: (\d{4}-\d{2}-\d{2})',
    'imie': r'Imię: (\w+)',
    'nazwisko': r'Nazwisko: (\w+)',
    'rok': r'Rok: (\d+)',
    'grupa': r'Grupa: (\w+)',
    'id_studenta': r'Id studenta: (\d+)',
    'pytanie': r'Pytanie:(.*?)\n',
    'domena': r'Domena: (.*?)$',
    'zrodla': r'Źródła: (.*?)\n',
    'tresc': r'Treść odpowiedzi:(.*)'
}

def read_txt(pdf_path):
    with open(pdf_path, 'r') as f:
        text = f.read()
    return text

def extract_information(text):
        # Dictionary to hold the extracted data
        extracted_data = {}
        # Search for each pattern in the text and extract the corresponding information
        for key, pattern in patterns.items():
            match = re.search(pattern, text, re.MULTILINE | re.DOTALL)
            if match:
                if match.group(1):
                    extracted_data[key] = match.group(1).strip()
        extracted_data['text'] = text
        return extracted_data

def read_all_files(pdf_directory):
    all_texts = ""
    db = Database(DB_FILE)
    for filename in os.listdir(pdf_directory):
        if filename.endswith('.pdf'):
            file_path = os.path.join(pdf_directory, filename)
            text = read_pdf(pdf_path)
        else if filename.endswith('.txt'):
            file_path = os.path.join(pdf_directory, filename)
            text = read_txt(pdf_path)
        info = extract_information(text)
        info['digest'] = str(calculate_digest(info['text']))
        info['nazwa_pliku'] = filename
        is_digest = db.session.query(
                Kolokwia
            ).filter_by(digest=info['digest']).first()
        if not is_digest:
            db.create_record(Kolokwia,info)
        all_texts += info['text']
    return all_texts


def test_file_read():
        all_text = read_all_files(pdf_directory)

if __name__ == "__main__":
    a = read_all_files()
    print('a : ', a )

