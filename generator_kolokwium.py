from utils import generate_pdf_from_string
from imchat import infer_chat
from obrobka_kolokwia import drukuj_wynik

KATALOG_SZTUCZNYCH_KOLOKWIOW = 'sztuczne_kolokwia/'

def prompt_kolokwium(temat_pracy):
    return f"""

Jako pilny student rozwiązań IoT napisz kolokwium.
Nie zapomnij podać źródeł z których korzystałeś!
Praca ma mieć następujący format:

Data: 2024-06-11
Imię: Tomasz
Nazwisko: Wawer
Rok: 3
Grupa: GR1
Id studenta: tu wpisz losową liczbę pięciocyfrową
Temat pracy: {temat_pracy}
Domena: sprzęt
Źródła: tu wpisz źródła z których korzystałeś!
Treść:

    tu wpisz treść odpowiedzi

"""

db_file = 'sqlite:///k143.db'
tem = drukuj_wynik(db_file)
for e,v in enumerate(tem):
    output_filepath = KATALOG_SZTUCZNYCH_KOLOKWIOW + f'{e}.pdf'
    text = infer_chat(prompt_kolokwium(v))
    generate_pdf_from_string(text, output_filepath)

