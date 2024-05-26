

import mysql.connector
from mysql.connector import Error

def connect(insert):
    """ Connect to MariaDB database """
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='siem_logs',
            user='siem',
            password='password'
        )

        if connection.is_connected():
            print('Connected to MariaDB database')

            # Create a cursor object using the cursor() method
            cursor = connection.cursor()

            # Execute SQL query using execute() method
            cursor.execute("SELECT DATABASE();")

            # Fetch a single row using fetchone() method
            record = cursor.fetchone()
            print("You're connected to database: ", record)


            cursor.execute(insert)
            connection.commit()
            print("Data inserted successfully")

            cursor.execute("SELECT * FROM raw_logs;")
            rows = cursor.fetchall()
            print("Data retrieved from the database:")
            for row in rows:
                print(row)

    except Error as e:
        print(f"Error: {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MariaDB connection is closed")


