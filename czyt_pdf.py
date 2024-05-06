import os
import re
from sqlalchemy import Column, Integer, String

from dbclass import Database, Base
from utils import calculate_digest, read_pdf

"""
Przeczytaj wszystkie pliki z folderu pdf_directory
Parsuj i policz digest dla każdego pliku i jeśli
unikalny umieść w tabeli
"""
# Directory containing the PDF files
pdf_directory = 'PlikiWejsciowe'

# plik sqlite3
DB_FILE = 'sqlite:///kolokwia.db'

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

class Kolokwia(Base):
    __tablename__ = 'kolokwia'

    id          = Column(Integer, primary_key=True)
    data        = Column(String)
    imie        = Column(String)
    nazwisko    = Column(String)
    rok         = Column(String)
    grupa       = Column(String)
    id_studenta = Column(String, nullable=False)
    digest      = Column(String)
    pytanie     = Column(String)
    domena      = Column(String)
    zrodla      = Column(String)
    tresc       = Column(String)
    text       = Column(String)

    def __repr__(self):
        return f"<MyModel(name='{self.name}', age={self.age})>"

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

