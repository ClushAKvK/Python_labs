import sqlite3
import datetime

entities = {'user': 'Пользователи', 'electronic': 'Электроника', 'basket': 'Корзина'}


ru_columns = {
    'user': ('ID', 'Имя', 'Фамилия'),
    'electronic': ('ID', 'Название', 'Производитель', 'Цена'),
    'basket': ('ID', 'ID-пользователя', 'ID-товара')
}


def open_connection():
    conn = sqlite3.connect('electronic.db')
    # cur = conn.cursor()
    # create_entities(conn, cur)
    return conn


def close_connection(conn):
    conn.close()


def create_entities(conn):
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS user(
            user_id INTEGER Primary key AUTOINCREMENT NOT NULL,
            first_name VARCHAR(150),
            last_name VARCHAR(150)
        )
    """)
    conn.commit()

    # cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS electronic(
            electronic_id INTEGER Primary key AUTOINCREMENT NOT NULL,
            title VARCHAR(150),
            manufacturer VARCHAR(150),
            price INTEGER(10)
        )
    """)
    conn.commit()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS basket(
            basket_id INTEGER Primary key AUTOINCREMENT NOT NULL,
            user_id INTEGER NOT NULL REFERENCES user(user_id) ON DELETE CASCADE,
            electronic_id INTEGER NOT NULL REFERENCES electronic(electronic_id) ON DELETE CASCADE
        )
    """)
    conn.commit()


def insert(conn, table, params):
    sql = f'INSERT INTO {table} VALUES(' + '?, ' * (len(params) - 1) + '?);'
    cur = conn.cursor()
    cur.execute(sql, params)
    conn.commit()


def insert_data(conn):
    data = {
        'user': {
            1: (1, 'Dmitri', 'Goblin'),
            2: (2, 'Rayan', 'Gosling'),
            3: (3, 'Kianno', 'Rivz')
        },
        'electronic': {
            0: (1, 'StreamCam', 'Logitech', 7580),
            1: (2, 'VSTARCAM CU2WIP', 'STARCAM', 3040),
            3: (3, 'Rekam A340', 'Rekam', 2790)
        },
        'basket': {
            1: (1, 1, 1),
            2: (2, 1, 2),
            3: (3, 1, 3),
            4: (4, 2, 1),
            5: (5, 3, 2),
            7: (6, 3, 3),
        }
    }

    for table, al_params in data.items():
        for params in al_params.values():
            insert(conn, table, params)


def select_all_from(conn, table):
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM {table}")
    data = cur.fetchall()
    return data


def delete_row_from(conn, table, row_id):
    cur = conn.cursor()
    cur.execute(f'DELETE FROM {table} WHERE {table}_id = {row_id};')
    conn.commit()