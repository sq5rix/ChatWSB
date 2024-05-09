from dbclass import Database, DB_FILE
from distance_text import policz_odleglosc
from imchat import infer_chat
from prompts import check_prompt, compare_prompt

db = Database(DB_FILE)

def przelicz_odleglosci(db):
    tresc_kolokwium = db.exec_query('select pytanie, tresc from kolokwia ')
    for i in tresc_kolokwium:
        tresc_ai = db.exec_query(f"select aitext from tematy where pytanie='{i[0].strip()}' ")
        for j in tresc_ai:
            dst = policz_odleglosc(i[1],j[0])
            print('dst : ', round(dst, 2))
            res = infer_chat(f"{check_prompt}: {i[1]}")
            print('res : ', res )
            res = infer_chat(f"{check_prompt}: {i[1]} {compare_prompt}{j[0]}")
            print('res : ', res )


przelicz_odleglosci(db)

