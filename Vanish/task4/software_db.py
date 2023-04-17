import sqlite3
import datetime

entities = {
    'company':          'Компания',
    'software':         'Программное обеспечение',
    'company_software': 'Компания-ПО'
}

ru_columns = {
    'company':          ('ID', 'Название', 'Слоган'),
    'software':         ('ID', 'Название', 'Описание', 'Цена'),
    'company_software': ('ID', 'Компания', 'Программное обеспечение')
}

en_columns = {
    'company':          ('ID', 'name', 'slogan'),
    'software':         ('ID', 'title', 'description', 'price'),
    'company_software': ('ID', 'company', 'software')
}


def open_connection():
    conn = sqlite3.connect('software.db')
    conn.execute("PRAGMA foreign_keys = 1")
    # cur = conn.cursor()
    # create_entities(conn, cur)
    return conn


def close_connection(conn):
    conn.close()


def create_entities(conn):
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS company(
            company_id INTEGER Primary key AUTOINCREMENT NOT NULL,
            name VARCHAR(150),
            slogan VARCHAR(150)
        )
    """)
    conn.commit()

    # cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS software(
            software_id INTEGER Primary key AUTOINCREMENT NOT NULL,
            title VARCHAR(150),
            description VARCHAR(150),
            price INTEGER(10)
        )
    """)
    conn.commit()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS company_software(
            company_software_id INTEGER Primary key AUTOINCREMENT NOT NULL,
            company_id INTEGER NOT NULL,
            software_id INTEGER NOT NULL,
            FOREIGN KEY (company_id) REFERENCES company(company_id) ON DELETE CASCADE,
            FOREIGN KEY (software_id) REFERENCES software(software_id) ON DELETE CASCADE
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
        'company': {
            1: (1, 'Microsoft', 'У нас всё летает'),
            2: (2, 'Биллайн', 'Живем на черной стороне'),
            3: (3, 'Epic Games', 'Мы движем индустрию...куда-то')
        },
        'software': {
            0: (1, 'Windows', 'лагает, зато без консольки да. ДОВОЛЬНЫ?!!', 10000),
            1: (2, 'Epic Games Store', 'я промолчу...', 0),
            3: (3, 'billain-identity', 'Ну ПО же? -ПО', 2790),
            4: (4, 'Microsoft Store', 'получше чем EGS', 0),
            5: (5, 'Unreal Engine', 'лучшие игровые движки', 7000),

        },
        'company_software': {
            1: (1, 1, 1),
            2: (2, 1, 4),
            3: (3, 2, 3),
            4: (4, 3, 3),
            5: (5, 3, 5)
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