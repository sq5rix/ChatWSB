import os
import re

from kolokwia import PDF_DIRECTORY
from utils import calculate_digest, read_pdf, read_text_file, read_real_pdf
from czyt_pdf import extract_information

from imchat import infer_chat
from prompts import check_prompt, compare_prompt, ocena_kolokwium

"""
Przeczytaj wszystkie pliki z folderu pdf_directory
Parsuj i policz digest dla każdego pliku i jeśli
unikalny umieść w tabeli
"""

# Regular expression patterns to match specific information
patterns = {
    'pytanie': r'[tT]emat [pP]racy:(.*?)[Dd]omena',
    'zrodla': r'[ŹźzZ]r[oó]d[lł]a: (.*?)Tre',
    'tresc': r'[tT]re[sś][cć]:(.*)',
}

def ocen_kolokwia(pdf_directory):
    all_texts = ""
    info = {}
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
            if info['tresc']:
                info['tresc'] = info['tresc'].strip()
                prompt_kol = ocena_kolokwium(info['pytanie'], info['tresc'], info.get('zrodla',''))
                odp = infer_chat(prompt_kol)
                print(info['nazwa_pliku'], odp)
            else:
                print('pusta tresc w ',info['nazwa_pliku'])
        except Exception as e:
            print('file_path : ', file_path )
            print(e)

def main():
    ocen_kolokwia(PDF_DIRECTORY)

if __name__ == "__main__":
    main()
