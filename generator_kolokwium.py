from utils import generate_pdf_from_string
from imchat import infer_chat
from dbclass import Database
from kolokwia import Tematy

KATALOG_SZTUCZNYCH_KOLOKWIOW = 'sztuczne_kolokwia/'

def prompt_kolokwium(temat_pracy):
    return f"""

Jako pilny student rozwiązań IoT napisz kolokwium używając poniższego formatu.
Nie stosuj żadnych znaków specjalnych, stosuj zwykły tekst.
Użyj co najmniej 5 punktów odpowiadających na zadany temat pracy. Potraktuj je jako nagłówki.
Opisz dokładnie każdy punkt pod nagłówkiem, w kilku zdaniach w polu Treść. Im dokładniej opiszesz kazdy z punktów, tym lepszą ocenę uzyskasz
Nie zapomnij podać źródeł z których korzystałeś! Dopisz je w polu źródła, nie umieszczaj ich w polu Treść
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

def pobierz_pytania(db_file):
    db = Database(db_file)
    tem = db.session.query(Tematy).all()
    for t in tem:
        try:
            print(t.pytanie)
        except:
            print('cos nie tak')
    return [t.pytanie for t in tem]

db_file = 'sqlite:///k143.db'
tem = pobierz_pytania(db_file)
for e,v in enumerate(tem[:20]):
    output_filepath = KATALOG_SZTUCZNYCH_KOLOKWIOW + f'{e}.pdf'
    text = infer_chat(prompt_kolokwium(v))
    generate_pdf_from_string(text, output_filepath)

