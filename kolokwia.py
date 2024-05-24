from sqlalchemy import Column, Integer, String
from sqlalchemy import UniqueConstraint, ForeignKey
from sqlalchemy.orm import relationship
from dbclass import Database, Base, DB_FILE

class Kolokwia(Base):
    __tablename__ = 'kolokwia'

    data        = Column(String)
    imie        = Column(String)
    nazwisko    = Column(String)
    rok         = Column(String)
    grupa       = Column(String)
    id_studenta = Column(String, nullable=False)
    digest      = Column(String, nullable=False, unique=True, primary_key=True)
    nazwa_pliku = Column(String)
    pytanie     = Column(String)
    domena      = Column(String)
    zrodla      = Column(String)
    tresc       = Column(String)
    text        = Column(String)

    def __repr__(self):
        return f"<MyModel(imie='{self.imie}', nazwisko={self.nazwisko})>"

class Tematy(Base):
    __tablename__ = 'tematy'
    id          = Column(Integer, primary_key=True)
    pytanie = Column(String, unique=True)
    aitext  = Column(String)

    def __repr__(self):
        return f"<MyModel(pytanie='{self.pytanie}', aitext={self.aitext})>"

#class Metryki(Base):
#    __tablename__ = 'tematy'
#    id = Column(Integer, primary_key=True)
#    kolokwium_id = Column(Integer)
#    temat_id     = Column(Integer)
#    distance     = Column(Integer)
#
#    def __repr__(self):
#        return f"<MyModel(pytanie='{self.pytanie}', aitext={self.aitext})>"



