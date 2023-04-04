from Saska.task4 import dbmusic

#!/usr/bin/env python3


# conn = dbmusic.open_connection()
# conn.close()

print("Content-type: text/html; charset=utf-8")
print()

print('<h2>Таблицы</h2>')
for en_entity, ru_entity in dbmusic.entities.items():
    print(f'<a href=/cgi-bin/tableDetail.py?table={en_entity}>{ru_entity}</a><br>')