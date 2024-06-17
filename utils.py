import hashlib
import pdfplumber
import pandas as pd
import chardet
import codecs
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont


def calculate_digest(input_string):
    # Encode the input string to bytes
    input_bytes = input_string.encode('utf-8')
    # Calculate the SHA-256 hash of the input bytes
    sha256_hash = hashlib.sha256(input_bytes)
    # Get the hexadecimal representation of the hash
    hex_digest = sha256_hash.hexdigest()
    # Convert the hexadecimal digest to an integer
    digest_number = int(hex_digest, 16)
    return digest_number

def read_real_pdf(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        text = ''
        for page in pdf.pages:
            text += page.extract_text() or ''
        return text

def read_pdf(pdf_path):
    try:
        with pdfplumber.open(pdf_path) as pdf:
            text = ''
            for page in pdf.pages:
                text += page.extract_text() or ''
        return text
    except:
        print('To nie jest pdf: ',pdf_path)
    try:
        text = read_text_file(pdf_path)
        return text
    except:
        print('To jest uszkodzony plik: ',pdf_path)

def read_text_file(file_path):
    # Detect file encoding
    with open(file_path, 'rb') as file:
        raw_data = file.read()
        result = chardet.detect(raw_data)
        encoding = result['encoding']
    # Read the file with detected encoding
    with codecs.open(file_path, 'r', encoding=encoding) as file:
        content = file.read()
    # Convert to UTF-8 if necessary
    if encoding.lower() != 'utf-8':
        content = content.encode('utf-8').decode('utf-8')
    return content

<<<<<<< HEAD

def generate_pdf_from_string(text, output_filepath):
    # Create a canvas object
    c = canvas.Canvas(output_filepath, pagesize=letter)

    # Set font and size
    pdfmetrics.registerFont(TTFont('Roboto', '/usr/share/fonts/TTF/Roboto-Medium.ttf'))
    c.setFont("Roboto", 12)

    # Split the text into lines
    lines = text.split('\n')

    # Set the initial y-coordinate for drawing text
    y = 750

    # Draw each line of text
    for line in lines:
        c.drawString(100, y, line)
        y -= 12  # Move to the next line

    # Save the canvas to a PDF file
    c.save()

def zapisz_slownik_do_excela(slownik, excel_name):
    df = pd.DataFrame(slownik)
    df.to_excel(excel_name)


def save_dict_to_excel(dct, excel_file_name):
    df = pd.DataFrame(dct)
    df.to_excel(excel_file_name)

def main():
    #input_string = "Hello, World!"
    #digest_number = calculate_digest(input_string)
    #print("Digest number of '{}' is: {}".format(input_string, digest_number))
    #file_path = 'DaneWrazliwe/drive-download-20240523T142544Z-001/Tyszka.txt'
    #file_content = read_text_file(file_path)
    #print(file_content)
    excel_name = 'excel.xlsx'
    slownik = [{'a':1, 'b':2}, {'a':2, 'b':3}]
    zapisz_slownik_do_excela(slownik, excel_name)

if __name__ == "__main__":
    main()
