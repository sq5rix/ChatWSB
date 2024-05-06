from sqlalchemy import Column, Integer, String
from dbclass import Database, Base

# plik sqlite3
DB_FILE = 'sqlite:///kolokwia.db'

class Kolokwia(Base):
    __tablename__ = 'kolokwia'

    id          = Column(Integer, primary_key=True)
    data        = Column(String)
    imie        = Column(String)
    nazwisko    = Column(String)
    rok         = Column(String)
    grupa       = Column(String)
    id_studenta = Column(String, nullable=False)
    digest      = Column(String)
    pytanie     = Column(String)
    domena      = Column(String)
    zrodla      = Column(String)
    tresc       = Column(String)
    text       = Column(String)

    def __repr__(self):
        return f"<MyModel(name='{self.name}', age={self.age})>"
