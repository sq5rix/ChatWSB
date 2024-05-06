from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Create an engine to connect to the database
engine = create_engine('sqlite:///example.db', echo=True)

# Create a base class for our models
Base = declarative_base()

# Define a model for our data
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

    def __repr__(self):
        return f"<User(name='{self.name}', age={self.age})>"

# Create the tables in the database
Base.metadata.create_all(engine)

# Create a CRUD database class
class Database:
    def __init__(self):
        # Create a session maker bound to our engine
        Session = sessionmaker(bind=engine)
        self.session = Session()

    def create_user(self, name, age):
        new_user = User(name=name, age=age)
        self.session.add(new_user)
        self.session.commit()
        return new_user

    def get_user(self, user_id):
        return self.session.get(User, user_id)

    def update_user(self, user_id, new_name=None, new_age=None):
        user = self.session.get(User,user_id)
        if user:
            if new_name:
                user.name = new_name
            if new_age:
                user.age = new_age
            self.session.commit()
            return user
        return None

    def delete_user(self, user_id):
        user = self.session.get(User, user_id)
        if user:
            self.session.delete(user)
            self.session.commit()
            return True
        return False

def main():
    db = Database()
    new_user = db.create_user("Alice", 30)
    print("Created user:", new_user)
    user = db.get_user(new_user.id)
    print("Retrieved user:", user)
    updated_user = db.update_user(new_user.id, new_name="Alice Smith")
    print("Updated user:", updated_user)
    deleted = db.delete_user(new_user.id)
    print("User deleted:", deleted)

if __name__ == "__main__":
    main()

