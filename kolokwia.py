from sqlalchemy import Column, Integer, String
from sqlalchemy import Column, Integer, String, UniqueConstraint
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
    digest      = Column(String, nullable=False, unique=True)
    pytanie     = Column(String)
    domena      = Column(String)
    zrodla      = Column(String)
    tresc       = Column(String, nullable=False, unique=True)
    text       = Column(String)
    __table_args__ = (
            UniqueConstraint(
                digest, name='idx_digest'),
         )


    def __repr__(self):
        return f"<MyModel(name='{self.name}', age={self.age})>"

#class Tematy(Base):
#    __tablename__ = 'kolokwia'
#
#    id          = Column(Integer, primary_key=True)
#    pytanie     = Column(String)
#    odp_chat    = Column(String)
#
#    def __repr__(self):
#        return f"<MyModel(name='{self.name}', age={self.age})>"
