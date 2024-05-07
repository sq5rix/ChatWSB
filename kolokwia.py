from sqlalchemy import Column, Integer, String
from sqlalchemy import UniqueConstraint, ForeignKey
from sqlalchemy.orm import relationship
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
    tresc       = Column(String, nullable=False)
    text        = Column(String)
    __table_args__ = (
            UniqueConstraint(
                digest, ),
         )


    def __repr__(self):
        return f"<MyModel(imie='{self.imie}', nazwisko={self.nazwisko})>"

class Tematy(Base):
    __tablename__ = 'tematy'

    id          = Column(Integer, primary_key=True)
    odp_chat    = Column(String)
    pytanie = Column(String, ForeignKey('kolokwia.pytanie'))
    kolokwium = relationship(Kolokwia)


    def __repr__(self):
        return f"<MyModel(name='{self.pytanie}', odp_chat={self.odp_chat})>"

