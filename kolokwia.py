from sqlalchemy import Column, Integer, String, PickleType
from sqlalchemy import UniqueConstraint, ForeignKey
from sqlalchemy.orm import relationship
from dbclass import Database, Base, DB_FILE

# Directory containing the PDF files
#PDF_DIRECTORY = 'PlikiWejsciowe'
#PDF_DIRECTORY = 'PlikiWejsciowe'
PDF_DIRECTORY = 'DaneWrazliwe/kolokwia_pdf/drive-download-20240524T155103Z-001/'

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
    distance    = Column(PickleType)

    def __repr__(self):
        return f"<MyModel(imie='{self.imie}', nazwisko={self.nazwisko})>"

class Tematy(Base):
    __tablename__ = 'tematy'
    temat_id = Column(Integer, primary_key=True)
    pytanie  = Column(String, unique=True)
    aitext   = Column(String)

    def __repr__(self):
        return f"<MyModel(pytanie='{self.pytanie}', aitext={self.aitext})>"

