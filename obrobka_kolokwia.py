from dbclass import Database, Base, DB_FILE
from kolokwia import Tematy
from prompts import odp_kolokwium_prompt
from imchat import infer_chat

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


def main():
    db = Database(DB_FILE)
    przelicz_pytania()
    sel = db.exec_query('select tresc from kolokwia')
    for i in sel:
        try:
            print('sel : ', i[0][:38] )
        except:
            print('cos nie tak')
    tem = db.exec_query('select aitext from tematy')
    for t in tem:
        try:
            print('tem : ', t[0].strip()[:38])
        except:
            print('cos nie tak')

if __name__ == "__main__":
    main()

