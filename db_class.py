import sqlite3
import psycopg2

class DatabaseAccess:
    def __init__(self, db_type, **kwargs):
        self.db_type = db_type
        if self.db_type == 'sqlite':
            self.connection = sqlite3.connect(kwargs.get('sqlite_file'))
        elif self.db_type == 'postgresql':
            self.connection = psycopg2.connect(
                dbname=kwargs.get('dbname'),
                user=kwargs.get('user'),
                password=kwargs.get('password'),
                host=kwargs.get('host'),
                port=kwargs.get('port')
            )
        else:
            raise ValueError("Unsupported database type. Please choose 'sqlite' or 'postgresql'.")

    def create(self, table, data):
        columns = ', '.join(data.keys())
        placeholders = ', '.join(['?' for _ in data])
        query = f"INSERT INTO {table} ({columns}) VALUES ({placeholders})"
        cursor = self.connection.cursor()
        cursor.execute(query, tuple(data.values()))
        self.connection.commit()
        return cursor.lastrowid

    def read(self, table, condition=None):
        query = f"SELECT * FROM {table}"
        if condition:
            query += f" WHERE {condition}"
        cursor = self.connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()

    def update(self, table, data, condition):
        set_clause = ', '.join([f"{key} = ?" for key in data.keys()])
        query = f"UPDATE {table} SET {set_clause} WHERE {condition}"
        cursor = self.connection.cursor()
        cursor.execute(query, tuple(data.values()))
        self.connection.commit()

    def delete(self, table, condition):
        query = f"DELETE FROM {table} WHERE {condition}"
        cursor = self.connection.cursor()
        cursor.execute(query)
        self.connection.commit()

    def close(self):
        self.connection.close()

def main():
# Create an instance of the DatabaseAccess class
    db = DatabaseAccess('sqlite', sqlite_file='example.db')

# Create a table if it doesn't exist
    db.create('users', {'name': 'John', 'age': 30})

# Insert a record into the table
    db.create('users', {'name': 'Alice', 'age': 25})

# Read records from the table
    users = db.read('users')
    print(users)

# Update a record
    db.update('users', {'age': 35}, 'name = "John"')

# Delete a record
    db.delete('users', 'name = "Alice"')

# Close the database connection
    db.close()

if __name__ == "__main__":
    main()
