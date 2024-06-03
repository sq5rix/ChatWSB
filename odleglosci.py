from dbclass import Database, DB_FILE
from distance_text import policz_odleglosc
from imchat import infer_chat
from prompts import check_prompt, compare_prompt
from scipy.spatial.distance import euclidean, braycurtis, chebyshev
from bleurouge import calculate_bleu
from distance_text import calculate_rouge_explain

db = Database(DB_FILE)

METRYKI = [euclidean, braycurtis, chebyshev]

def classic(text1, text2, fun):
    for fun in METRYKI:
        try:
            dst = policz_odleglosc(text1, text2, fun)
            print('dst : ', fun.__name__, dst)
        except:
            print('błąd')

def infer(text1, text2):
    res = infer_chat(f"{check_prompt}: {text1}")
    print('res : ', res )
    res = infer_chat(f"{check_prompt}: {text1} {compare_prompt}{text2}")
    print('res : ', res )

def przelicz_odleglosci(db):
    tresc_kolokwium = db.exec_query('select pytanie, tresc, nazwa_pliku  from kolokwia ')
    for i in tresc_kolokwium:
        print('nazwa_pliku  : ', i[2])
        if i[0]:
            tresc_ai = db.exec_query(f"select aitext from tematy where pytanie='{i[0].strip()}' ")
        else:
            tresc_ai = []
        for j in tresc_ai:
            #classic(i[1], j[0], fun)
            #infer(i[1], j[0])
            calculate_rouge_explain(j[0], i[1])


def main():
    przelicz_odleglosci(db)

if __name__ == "__main__":
    main()

