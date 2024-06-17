import json
from pprint import pprint
from dbclass import Database, Base, DB_FILE
from czyt_pdf import read_all_files
from kolokwia import Tematy, PDF_DIRECTORY, Kolokwia
from prompts import odp_kolokwium_prompt
from imchat import infer_chat
from odleglosci import przelicz_odleglosci
from utils import save_dict_to_excel

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
        print(i.nazwisko, i.distance)
    #tem = db.exec_query('select aitext from tematy')
    #for t in tem:
    #    try:
    #        print('tem : ', t[0].strip()[:38])
    #    except:
    #        print('cos nie tak')

def parsuj_wynik(string_to_parse):
    parsed_dict = {}
    pairs = string_to_parse.split(',')
    for pair in pairs:
        pair = pair.strip()
        if ':' in pair:
            key, value = pair.split(':')
            value = int(value.strip().replace('.',''))
            parsed_dict[key] = int(value)  # Convert value to int if necessary
    return parsed_dict


def dodaj_odleglosci():
    odl = przelicz_odleglosci()

def wyciagnij_slownik_odleglosci():
    db = Database(DB_FILE)
    sel = db.session.query(Kolokwia).all()
    a = []
    for i in sel:
        x = i.distance
        if x:
            x.update({'nazwa':i.nazwa_pliku})
            d = parsuj_wynik(x.get('ocenaGPT', None))
            if d:
                x.update(d)
                del x['ocenaGPT']
            a.append(x)
    return a

def main():
    db = Database(DB_FILE)
    #txt = read_all_files(PDF_DIRECTORY)
    #przelicz_pytania()
    #dodaj_odleglosci()
    #drukuj_wynik()
    odl = wyciagnij_slownik_odleglosci()
    save_dict_to_excel(odl, 'DaneWrazliwe/wyniki.xlsx')

if __name__ == "__main__":
    main()

