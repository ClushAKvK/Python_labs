import cgi

from Saska.task4 import dbmusic
from Saska.task4.xmlmusic import tags
# from index import entities

form = cgi.FieldStorage()
table_name = form.getvalue('table')

conn = dbmusic.open_connection()

if form.getvalue(tags[table_name][0]) is not None:
    params = []
    for tag in tags[table_name]:
        params.append(form.getvalue(tag))
    dbmusic.insert(conn, table_name, params)

if form.getvalue('del_line') is not None:
    dbmusic.delete_record_from(conn, table_name, form.getvalue('del_line'))

table = dbmusic.get_all_from(conn, table_name)
conn.close()

print("Content-type: text/html; charset=utf-8")
print()

print(f'<h3>Таблица: {dbmusic.entities[table_name]}</h3>')
for record in table:
    print(f'<span>{record}</span> <a href="/cgi-bin/tableDetail.py?table={table_name}&del_line={record[0]}">Удалить запись</a><br>')

print(f'<form action="/cgi-bin/tableDetail.py?table={table_name}" method="POST">')
for tag in tags[table_name]:
    print(f'<input type="text" name="{tag}" />')
print(f'<input type="submit" value="Добавить" />')
print(f'</form>')
print(f'<a href="/cgi-bin/index.py">На главную</a>')
