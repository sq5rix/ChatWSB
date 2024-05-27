from dbclass import Database, DB_FILE
from distance_text import policz_odleglosc
from imchat import infer_chat
from prompts import check_prompt, compare_prompt
from scipy.spatial.distance import euclidean, braycurtis, chebyshev
from bleurouge import calculate_bleu, calculate_rouge

db = Database(DB_FILE)

METRYKI = [calculate_bleu, calculate_rouge, euclidean, braycurtis, chebyshev]
#METRYKI = [calculate_rouge, euclidean, braycurtis, chebyshev]

def przelicz_odleglosci(db):
    tresc_kolokwium = db.exec_query('select pytanie, tresc, nazwa_pliku  from kolokwia ')
    for i in tresc_kolokwium:
        print('nazwa_pliku  : ', i[2])
        if i[0]:
            tresc_ai = db.exec_query(f"select aitext from tematy where pytanie='{i[0].strip()}' ")
        else:
            tresc_ai
        for j in tresc_ai:
            for fun in METRYKI:
                try:
                    dst = policz_odleglosc(i[1], j[0], fun)
                    print('dst : ', fun.__name__, dst)
                except:
                    print('błąd')
            #res = infer_chat(f"{check_prompt}: {i[1]}")
            #print('res : ', res )
            #res = infer_chat(f"{check_prompt}: {i[1]} {compare_prompt}{j[0]}")
            #print('res : ', res )


przelicz_odleglosci(db)

