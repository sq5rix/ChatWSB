from dbclass import Database, Base
from kolokwia import Tematy, DB_FILE
from prompts import odp_kolokwium_prompt

def przelicz_pytanie():
    db = Database(DB_FILE)
    db.create_table(Tematy)
    sel = db.exec_query('select distinct pytanie from kolokwia')
    for i in sel:
        print('i : ', i[0])
        is_pytanie = db.session.query(
                Tematy
            ).filter_by(pytanie=i[0]).first()
        if not is_pytanie:
            db.create_record(Tematy, {'pytanie':i[0]})
        rec = db.session.query(
                Tematy
            ).filter_by(pytanie=i[0]).first()
        print('rec : ', rec )
        if not rec:
            odp = f"{odp_kolokwium_prompt}{i[0]}"
            print('odp : ', odp )
            db.update_record(Tematy, rec, {'aitext':odp})


def main():
    db = Database(DB_FILE)
    przelicz_pytanie()
    #sel = db.exec_query('select aitext from kolokwia')
    #for i in sel:
    #    print('sel : ', i[0][:38] )
    sel = db.exec_query('select aitext from tematy')
    for i in sel:
        print('sel : ', i[0])

if __name__ == "__main__":
    main()

