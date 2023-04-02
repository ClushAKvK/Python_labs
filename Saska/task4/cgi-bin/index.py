from Saska.task4 import dbmusic

#!/usr/bin/env python3

conn = dbmusic.open_connection()
users = dbmusic.get_users(conn)
conn.close()
# print(users)

print("Content-type: text/html")
print()
for user in users:
    idx = f'{user[0]}'
    FIO = f'{user[1]} {user[2]}'
    playlist_size = f'{user[3]}'

    print(f'<span>{idx}: </span>')
    print(f'<a href="http://localhost:8000/cgi-bin/users/detail{idx}.py">{FIO}</a>')
    print(f'<span>Amount of tracks in playlist: {playlist_size} </span>')
    print('<br>')