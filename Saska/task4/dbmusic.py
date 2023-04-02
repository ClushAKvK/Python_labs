import sqlite3
import datetime


def open_connection():
    conn = sqlite3.connect('music.db')
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
            last_name VARCHAR(150),
            playlist_size INTEGER
        )
    """)
    conn.commit()

    # cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS track(
            track_id INTEGER Primary key AUTOINCREMENT NOT NULL,
            album_id INTEGER NOT NULL REFERENCES album(album_id),
            title VARCHAR(150),
            singer VARCHAR(150),
            duration TIME
        )
    """)
    conn.commit()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS user_playlist(
            user_id INTEGER NOT NULL REFERENCES user(user_id),
            track_id INTEGER NOT NULL REFERENCES track(track_id),
            PRIMARY KEY (user_id, track_id)
        )
    """)
    conn.commit()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS album(
            album_id INTEGER Primary key AUTOINCREMENT NOT NULL,
            title VARCHAR(150),
            description TEXT,
            published_date DATE
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
            1: (1, 'Alex', 'Shirko', 12),
            2: (2, 'Semen', 'Mahalin', 5),
            3: (3, 'Ivan', 'Pozdnyakov', 4),
            4: (4, 'Kirill', 'Kuzmin', 1),
            5: (5, 'Ilya', 'Molchanov', 4)
        },
        'album': {
            0: (1, 'Single', 'Single', None),
            1: (2, 'Elevation', 'alternative metal', datetime.date(2016, 1, 1)),
            3: (3, 'Monuments', 'alternative metal', datetime.date(2016, 10, 11)),
            4: (4, 'Ephemeral', 'alternative metal', datetime.date(2019, 1, 1))
        },
        'track': {
            1: (1, 2, 'Delusion', 'We Are The Catalyst', f'{datetime.time(0, 3, 50)}'),
            2: (2, 2, 'Open Door', 'We Are The Catalyst', f'{datetime.time(0, 3, 34)}'),
            3: (3, 2, 'One More Day', 'We Are The Catalyst', f'{datetime.time(0, 3, 28)}'),
            4: (4, 2, 'Askja', 'We Are The Catalyst', f'{datetime.time(0, 4, 2)}'),
            5: (5, 3, 'Our Way to the Sun', 'We Are The Catalyst', f'{datetime.time(0, 4, 3)}'),
            6: (6, 3, 'Not Alone', 'We Are The Catalyst', f'{datetime.time(0, 5, 8)}'),
            7: (7, 3, 'Don’t You Worry Child', 'We Are The Catalyst', f'{datetime.time(0, 4, 27)}'),
            8: (8, 4, 'The Code', 'We Are The Catalyst', f'{datetime.time(0, 3, 9)}'),
            9: (9, 4, 'In Shadows', 'We Are The Catalyst', f'{datetime.time(0, 3, 30)}'),
            10: (10, 4, 'Dust', 'We Are The Catalyst', f'{datetime.time(0, 3, 48)}'),
            11: (11, 1, 'Losing My Mind', 'We Are The Catalyst', f'{datetime.time(0, 3, 15)}'),
            12: (12, 1, 'Blinding Lights', 'We Are The Catalyst', f'{datetime.time(0, 3, 17)}')
        },
        'user_playlist': {
            1: (1, 1),
            2: (1, 2),
            3: (1, 3),
            4: (1, 4),
            5: (1, 5),
            7: (1, 6),
            8: (1, 7),
            9: (1, 8),
            10: (1, 9),
            11: (1, 10),
            12: (1, 11),
            13: (1, 12),
            14: (2, 11),
            15: (2, 1),
            16: (2, 3),
            17: (2, 5),
            18: (2, 7),
            19: (3, 9),
            20: (3, 11),
            21: (3, 1),
            22: (3, 2),
            23: (4, 3),
            24: (5, 5),
            25: (5, 6),
            26: (5, 12),
            27: (5, 4),
        }
    }

    for table, al_params in data.items():
        for params in al_params.values():
            insert(conn, table, params)


def get_users(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM user;")
    all_users = cur.fetchall()
    return all_users


def get_playlist_of(conn, user_id):
    cur = conn.cursor()
    cur.execute("""
        SELECT tr.* from user us
            JOIN user_playlist up ON up.user_id = us.user_id and us.user_id = {}
            JOIN track tr ON up.track_id = tr.track_id;
    """.format(user_id))
    all_tracks = cur.fetchall()
    return all_tracks


def get_album(conn, album_id):
    cur = conn.cursor()
    cur.execute("""
            SELECT * FROM album al
                WHERE al.album_id = {0}
        """.format(album_id))
    album_title = cur.fetchone()
    return album_title


def get_all_from(conn, table):
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM {table}")
    data = cur.fetchall()
    return data
