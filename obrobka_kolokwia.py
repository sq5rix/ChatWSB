from dbclass import Database, Base
from kolokwia import Tematy, Kolokwia, DB_FILE

def main():
    db = Database(Kolokwia, DB_FILE)
    sel = db.exec_query('select digest from kolokwia')
    for i in sel:
        print('sel : ', i[0][:18] )
    #sel = db.exec_query('select pytanie from tematy')
    #for i in sel:
    #    print('sel : ', i[0][:18] )

if __name__ == "__main__":
    all = main()

