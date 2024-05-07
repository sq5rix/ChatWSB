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
    'tresc': r'Treść.*?:(.*?)\n'
}


def extract_information(pdf_path):
        # Dictionary to hold the extracted data
        text = read_pdf(pdf_path)
        extracted_data = {}
        # Search for each pattern in the text and extract the corresponding information
        for key, pattern in patterns.items():
            match = re.search(pattern, text, re.MULTILINE | re.DOTALL)
            if match:
                if match.group(1):
                    extracted_data[key] = match.group(1).strip()
        extracted_data['text'] = text
        return extracted_data

def read_all_files():
    all_texts = ""
    db = Database(Kolokwia, DB_FILE)
    #db.truncate_table()
    for filename in os.listdir(pdf_directory):
        if filename.endswith('.pdf'):
            file_path = os.path.join(pdf_directory, filename)
            info = extract_information(file_path)
            info['digest'] = str(calculate_digest(info['text']))
            db.create_record(info)
            all_texts += info['text']
    sel = db.exec_query('select * from kolokwia')
    for i in sel:
        print('sel : ', i )
    return all_texts

if __name__ == "__main__":
    all = read_all_files()

