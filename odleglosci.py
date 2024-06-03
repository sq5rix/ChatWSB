from dbclass import Database, DB_FILE
from kolokwia import Kolokwia
from distance_text import policz_odleglosc
from imchat import infer_chat
from prompts import check_prompt, compare_prompt
from scipy.spatial.distance import euclidean, braycurtis, chebyshev
from bleurouge import calculate_bleu
from distance_text import calculate_rouge_explain

METRYKI = [euclidean, braycurtis, chebyshev]

def classic_measurement(text1, text2):
    dst = {}
    for fun in METRYKI:
        try:
            dst[fun.__name__] = policz_odleglosc(text1, text2, fun)
        except:
            print('błąd')
    return dst

def infer(text1, text2):
    res = infer_chat(f"{check_prompt}: {text1}")
    print('res : ', res )
    res = infer_chat(f"{check_prompt}: {text1} {compare_prompt}{text2}")
    print('res : ', res )


def policz_odleglosc_tekstow(text_studenta, text_ai):
    """
    liczy odległość tekstów metodami klasycznymi
    oraz testuje klasyfikacją rouge
    """
    dst = classic_measurement(text_studenta, text_ai)
    #infer(i[1], j[0])
    cal = calculate_rouge_explain(text_ai, text_studenta)
    if cal:
        dst.update(cal)
    return dst

def update_record(db, dig, wyn):
    db.session.query(Kolokwia).\
        filter(Kolokwia.digest == dig).\
        update({'distance': wyn})
    db.session.commit()


def przelicz_odleglosci():
    db = Database(DB_FILE)
    tresc_kolokwium = db.exec_query('select pytanie, tresc, nazwa_pliku, digest  from kolokwia ')
    for i in tresc_kolokwium:
        print('nazwa_pliku  : ', i[2])
        if i[0]:
            tresc_ai = db.exec_query(f"select aitext from tematy where pytanie='{i[0].strip()}' ")
        else:
            tresc_ai = []
        for j in tresc_ai:
            wyniki = policz_odleglosc_tekstow(i[1], j[0])
            print('wyniki : ', wyniki )
            update_record(db, i[3], wyniki)


def main():
    przelicz_odleglosci()

if __name__ == "__main__":
    main()

