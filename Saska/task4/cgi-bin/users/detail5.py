from Saska.task4 import dbmusic

conn = dbmusic.open_connection()
tracks = dbmusic.get_playlist_of(conn, 5)
# conn.close()

print("Content-type: text/html")
print()

for track in tracks:
    idx = f'{track[0]}'
    album_name = f'{dbmusic.get_album(conn, track[1])[1]}'
    track_title = f'{track[2]}'
    singer = f'{track[3]}'
    duration = f'{track[4]}'

    print(f'<span>{idx}: {track_title}(album: </span>')
    print(f'<a href="http://localhost:8000/cgi-bin/albums/album{track[1]}.py">{album_name}</a>')
    print(f'<span>) Singer: {singer} Duration: {duration}</span>')
    print('<br>')

conn.close()