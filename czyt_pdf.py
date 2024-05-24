import os
import re

from dbclass import Database, Base
from kolokwia import Kolokwia, DB_FILE
from utils import calculate_digest, read_pdf, read_text_file

"""
Przeczytaj wszystkie pliki z folderu pdf_directory
Parsuj i policz digest dla każdego pliku i jeśli
unikalny umieść w tabeli
"""
# Directory containing the PDF files
#pdf_directory = 'PlikiWejsciowe'
#pdf_directory = 'PlikiWejsciowe'
pdf_directory = 'DaneWrazliwe/kolokwia_pdf/drive-download-20240524T155103Z-001/'

# Regular expression patterns to match specific information
patterns = {
    'data': r'Data: (\d{4}-\d{2}-\d{2})',
    'imie': r'Imię: (\w+)',
    'nazwisko': r'Nazwisko: (\w+)',
    'rok': r'Rok: (\d+)$',
    'grupa': r'Grupa: (\w+)$',
    'id_studenta': r'[iI][Dd][ _][Ss]tudent.*?:\s*?(\d+)',
    'pytanie': r'Pytanie:(.*?)\n',
    'domena': r'Domena: (.*?)',
    'zrodla': r'Źródła: (.*?)\n',
    'tresc': r'Tre[sś][cć] [Oo]dpowiedzi:(.*)'
}

def extract_information(text):
        # Dictionary to hold the extracted data
        extracted_data = {}
        extracted_data['text'] = text
        # Search for each pattern in the text and extract the corresponding information
        for key, pattern in patterns.items():
            match = re.search(pattern, text, re.MULTILINE | re.DOTALL)
            if match:
                if match.group(1):
                    extracted_data[key] = match.group(1).strip()
        return extracted_data

def utworz_rzad_tabeli(db, info):
    is_digest = db.session.query(
            Kolokwia
        ).filter_by(digest=info['digest']).first()
    if not is_digest:
        db.create_record(Kolokwia,info)

def read_all_files(pdf_directory):
    all_texts = ""
    db = Database(DB_FILE)
    for filename in os.listdir(pdf_directory):
        if filename.endswith('.pdf'):
            file_path = os.path.join(pdf_directory, filename)
            text = read_pdf(file_path)
        elif filename.endswith('.txt'):
            file_path = os.path.join(pdf_directory, filename)
            text = read_text_file(file_path)
        try:
            info = extract_information(text)
            info['nazwa_pliku'] = filename
            info['digest'] = str(calculate_digest(text))
        except Exception as e:
            print('file_path : ', file_path )
            print(e)
        try:
            utworz_rzad_tabeli(db, info)
        except Exception as e:
            print('file_path : ', file_path )
            print(e)


def test_file_read():
        read_all_files(pdf_directory)

if __name__ == "__main__":
    all_text = read_all_files(pdf_directory)

