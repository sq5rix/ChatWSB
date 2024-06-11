from sqlalchemy import Column, Integer, Text, PickleType
from sqlalchemy import UniqueConstraint, ForeignKey
from sqlalchemy.orm import relationship
from dbclass import Database, Base, DB_FILE

# Directory containing the PDF files
#PDF_DIRECTORY = 'PlikiWejsciowe'
#PDF_DIRECTORY = 'PlikiWejsciowe'
#PDF_DIRECTORY = 'DaneWrazliwe/kolokwia_pdf/drive-download-20240524T155103Z-001/'
#PDF_DIRECTORY = 'DaneWrazliwe/drive-download-20240608T095515Z-001'
PDF_DIRECTORY = 'sztuczne_kolokwia/'

class Kolokwia(Base):
    __tablename__ = 'kolokwia'

    data        = Column(Text)
    imie        = Column(Text)
    nazwisko    = Column(Text)
    rok         = Column(Text)
    grupa       = Column(Text)
    id_studenta = Column(Text)
    digest      = Column(Text, nullable=False, unique=True, primary_key=True)
    nazwa_pliku = Column(Text)
    pytanie     = Column(Text)
    domena      = Column(Text)
    zrodla      = Column(Text)
    tresc       = Column(Text)
    text        = Column(Text)
    distance    = Column(PickleType)

    def __repr__(self):
        return f"<MyModel(imie='{self.imie}', nazwisko={self.nazwisko})>"

class Tematy(Base):
    __tablename__ = 'tematy'
    temat_id = Column(Integer, primary_key=True)
    pytanie  = Column(Text, unique=True)
    aitext   = Column(Text)

    def __repr__(self):
        return f"<MyModel(pytanie='{self.pytanie}', aitext={self.aitext})>"

