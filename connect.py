import psycopg2
from psycopg2 import Error

def connect_to_db():
    connection = psycopg2.connect(
        database="loyalty_db",
        user="postgres",
        password="123456",
        host="localhost",
        port="5433"
    )
    print("Connection to the database established successfully.")
    return connection
if __name__ == "__main__":
    try:
        conn = connect_to_db()
    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL", error)
    finally:
        if conn:
            conn.close()
            print("PostgreSQL connection is closed.")