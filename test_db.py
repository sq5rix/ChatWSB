from sqlalchemy import Column, Integer, String
from dbclass import Base, Database

DB_FILE = 'sqlite:///example.db'

class MyModel(Base):
    __tablename__ = 'mymodels'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

    def __repr__(self):
        return f"<MyModel(name='{self.name}', age={self.age})>"

# Example usage
db = Database(MyModel, DB_FILE)
id = db.create_record({'name':'john','age':20})
rec = db.get_record(id)
print('rec : ', rec )
al = db.find_by_value('name','john')
print('al : ', al )
sel = db.exec_query('select * from mymodels')
