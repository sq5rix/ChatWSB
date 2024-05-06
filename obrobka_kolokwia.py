from dbclass import Database, Base
from kolokwia import Kolokwia, DB_FILE

def main():
    db = Database(Kolokwia, DB_FILE)
    sel = db.exec_query('select id_studenta from kolokwia')
    for i in sel:
        print('sel : ', i[0] )

if __name__ == "__main__":
    all = main()


