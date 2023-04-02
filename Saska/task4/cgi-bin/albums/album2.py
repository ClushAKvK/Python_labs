from Saska.task4 import dbmusic

conn = dbmusic.open_connection()
album = dbmusic.get_album(conn, 2)
conn.close()

print("Content-type: text/html")
print()

idx = f'{album[0]}'
title = f'{album[1]}'
description = f'{album[2]}'
pub_date = f'{album[3]}'

print(f"<h1>{title}</h1><br>")
print(f'<span>Index: {idx}</span><br>')
print(f'<span>Description: {description}</span><br>')
print(f'<span>Was published in: {pub_date}</span><br>')
