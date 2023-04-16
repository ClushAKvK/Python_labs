import cgi

from Mlechni.task4 import electronicdb

# from index import entities

form = cgi.FieldStorage()
table_name = form.getvalue('table')

conn = electronicdb.open_connection()

if form.getvalue('last_row') is not None:
    params = [int(form.getvalue('last_row')) + 1]
    for tag in electronicdb.ru_columns[table_name]:
        if tag == 'ID': continue
        params.append(form.getvalue(tag))
    electronicdb.insert(conn, table_name, params)

if form.getvalue('del_line') is not None:
    electronicdb.delete_row_from(conn, table_name, form.getvalue('del_line'))

data = electronicdb.select_all_from(conn, table_name)
# conn.close()

print("Content-type: text/html; charset=utf-8")
print()

print('<table>')

print(f'<caption><h2>{electronicdb.entities[table_name]}</h2></caption>')
print('<tr>')
for column in electronicdb.ru_columns[table_name]:
    print(f'<th>{column}</th>')
print('<tr>')

for record in data:
    print('<tr>')
    for obj in record:
        pass
        print(f'<td>{obj}</td>')
    print(f'<td><a href="/cgi-bin/tableDetail.py?table={table_name}&del_line={record[0]}">удалить</a></td>')
    print('</tr>')

print('<tr>')
print('<td>-</td>')

print(f'<form action="/cgi-bin/tableDetail.py?table={table_name}&last_row={data[len(data) - 1][0]}" method="POST">')
if table_name == 'basket':
    tags = electronicdb.ru_columns[table_name]

    print(f'<td><select name={tags[1]}>')
    for user in electronicdb.select_all_from(conn, 'user'):
        print(f'<option value="{user[0]}">{f"{user[1]} {user[2]}"}</option>')
    print('</select></td>')

    print(f'<td><select name={tags[2]}>')
    for elec in electronicdb.select_all_from(conn, 'electronic'):
        print(f'<option value="{elec[0]}">{elec[1]}</option>')
    print('</select></td>')
else:
    for tag in electronicdb.ru_columns[table_name]:
        if tag == 'ID': continue
        print(f'<td><input type="text" name="{tag}" /></td>')
print(f'<td><button type="submit">добавить</button></td>')
print('</form>')

print('</tr>')

print('</table>')

print(f'<a href="/cgi-bin/index.py">На главную</a>')

conn.close()