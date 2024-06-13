import os
import re

from dbclass import Database, Base
from kolokwia import Kolokwia, DB_FILE, PDF_DIRECTORY
from utils import calculate_digest, read_pdf, read_text_file, read_real_pdf

"""
Przeczytaj wszystkie pliki z folderu pdf_directory
Parsuj i policz digest dla każdego pliku i jeśli
unikalny umieść w tabeli
"""

# Regular expression patterns to match specific information
patterns = {
    'data': r'[dD]ata: (\d{4}-\d{2}-\d{2})',
    'imie': r'[iI]mię: (\w+)',
    'nazwisko': r'Nazwisko: (\w+)',
    'rok': r'Rok: (\d+)$',
    'grupa': r'[gG]rupa: (.*?)[iI][Dd]',
    'id_studenta': r'[iI][Dd][ _][Ss]tudenta:\s*?(\d+)$',
    'pytanie': r'[tT]emat [pP]racy:(.*?)[Dd]omena',
    'domena': r'[dD]omena:(.*?)[ŹźzZ]r[óo]d[lł]a',
    'zrodla': r'[ŹźzZ]r[oó]d[lł]a: (.*?)Tre',
    'tresc': r'[tT]re[sś][cć]:(.*)',
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
        rec = db.create_record(Kolokwia,info)
        print('rec : ', rec )

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
        else:
            continue
        try:
            info = extract_information(text)
            info['nazwa_pliku'] = filename
            info['digest'] = str(calculate_digest(text))
            if info['tresc']:
                info['tresc'] = info['tresc'].strip()
            else:
                print('pusta tresc w ',info['nazwa_pliku'])
        except Exception as e:
            print('file_path : ', file_path )
            print(e)
        try:
            utworz_rzad_tabeli(db, info)
        except Exception as e:
            print('file_path : ', file_path )
            print(e)

def read_one_files(pdf_directory, filename):
    db = Database(DB_FILE)
    all_texts = ""
    file_path = os.path.join(pdf_directory, filename)
    #text = read_pdf(file_path)
    text = read_real_pdf(file_path)
    print('text : ', text)
    if not text:
        return
    info = extract_information(text)
    info['nazwa_pliku'] = filename
    info['digest'] = str(calculate_digest(text))
    print('info["pytanie"]: ', info['pytanie'])
    utworz_rzad_tabeli(db, info)

def test_file_read():
        read_all_files(PDF_DIRECTORY)

if __name__ == "__main__":
    read_one_files(PDF_DIRECTORY, 'Sylwia_Sulkowska_139.pdf')
    #all_text = read_all_files(pdf_directory)

