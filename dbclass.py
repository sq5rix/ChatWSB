from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Database:
    def __init__(self, model_class, db_url='sqlite:///:memory:'):
        self.engine = create_engine(db_url)
        self.model_class = model_class
        Base.metadata.create_all(self.engine)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    def create_record(self, values):
        record = self.model_class(**values)
        self.session.add(record)
        self.session.commit()
        return record.id

    def get_record(self, record_id):
        return self.session.get(self.model_class, record_id)

    def update_record(self, record_id, new_values):
        record = self.get_record(record_id)
        if record:
            for key, value in new_values.items():
                setattr(record, key, value)
            self.session.commit()
            return record
        return None

    def delete_record(self, record_id):
        record = self.get_record(record_id)
        if record:
            self.session.delete(record)
            self.session.commit()
            return True
        return False

    def find_by_value(self, attribute, value):
        # Query the session for records where the specified attribute matches the given value
        return self.session.query(self.model_class).filter(getattr(self.model_class, attribute) == value).all()
