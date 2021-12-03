import sqlite3
from sqlite3 import Error

a=input('Введите название таблицы: ')

PATH = 'Test.db'

def create_connection():
    connection = None
    try:
        connection = sqlite3.connect(PATH)
        print('Try to connect to db')
    except Error as e:
        print('Can`t connected. Error:', e)
    else:
        print("Success")

    return connection

def get_data(connection):
    cursor = connection.cursor()

    add_query = '''
            SELECT * FROM ,a,
            '''

    cursor.execute(add_query)
    records = cursor.fetchall()
    print(records)
    cursor.close()

conn = create_connection()
get_data(conn)