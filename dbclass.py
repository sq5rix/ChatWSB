from sqlalchemy import create_engine, Column, Integer, String, text
from sqlalchemy.orm import sessionmaker, declarative_base

Base = declarative_base()

class Database:
    def __init__(self, db_url='sqlite:///:memory:'):
        self.engine = create_engine(db_url)
        Base.metadata.create_all(self.engine)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    def create_record(self, model_class, values):
        record = model_class(**values)
        self.session.add(record)
        self.session.commit()
        return record

    def get_record(self, model_class, record_id):
        return self.session.get(model_class, record_id)

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

    def truncate_table(self, model_class):
        self.session.execute(text(f"DELETE FROM {model_class.__tablename__}"))
        self.session.commit()

    def find_by_value(self, model_class, attribute, value):
        # Query the session for records where the specified attribute matches the given value
        return self.session.query(model_class).filter(getattr(model_class, attribute) == value).all()

    def exec_query(self, query_string):
        return self.session.execute(text(query_string))

