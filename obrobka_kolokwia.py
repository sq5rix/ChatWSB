import json
from pprint import pprint
from dbclass import Database, Base, DB_FILE
from czyt_pdf import read_all_files
from kolokwia import Tematy, PDF_DIRECTORY, Kolokwia
from prompts import odp_kolokwium_prompt
from imchat import infer_chat
from odleglosci import przelicz_odleglosci

def przelicz_pytania():
    db = Database(DB_FILE)
    sel = db.exec_query('select distinct pytanie from kolokwia')
    for i in sel:
        is_pytanie = db.session.query(
                Tematy
            ).filter_by(pytanie=i[0]).first()
        if not is_pytanie:
            odp = infer_chat(f"{odp_kolokwium_prompt}{i[0]}") if i[0] else None
            print('odp : ', odp )
            db.create_record(Tematy, {'pytanie':i[0], 'aitext':odp})

def drukuj_wynik():
    db = Database(DB_FILE)
    sel = db.session.query(Kolokwia).all()
    for i in sel:
        print(i.nazwa_pliku, i.distance)
    #tem = db.exec_query('select aitext from tematy')
    #for t in tem:
    #    try:
    #        print('tem : ', t[0].strip()[:38])
    #    except:
    #        print('cos nie tak')

def dodaj_odleglosci():
    odl = przelicz_odleglosci()


def main():
    db = Database(DB_FILE)
    #txt = read_all_files(PDF_DIRECTORY)
    #przelicz_pytania()
    #dodaj_odleglosci()
    drukuj_wynik()

if __name__ == "__main__":
    main()

