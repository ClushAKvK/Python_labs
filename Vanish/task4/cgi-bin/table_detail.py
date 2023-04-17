import cgi

from Vanish.task4 import software_db

# from index import entities

form = cgi.FieldStorage()
table_name = form.getvalue('table')

conn = software_db.open_connection()

if form.getvalue('last_row') is not None:
    params = [int(form.getvalue('last_row')) + 1]
    for tag in software_db.en_columns[table_name]:
        if tag == 'ID': continue
        params.append(form.getvalue(tag))
    software_db.insert(conn, table_name, params)

if form.getvalue('del_line') is not None:
    software_db.delete_row_from(conn, table_name, form.getvalue('del_line'))

data = software_db.select_all_from(conn, table_name)
# conn.close()

print("Content-type: text/html; charset=utf-8")
print()

print('<table>')

print(f'<caption><h2>{software_db.entities[table_name]}</h2></caption>')
print('<tr>')
for column in software_db.ru_columns[table_name]:
    print(f'<th>{column}</th>')
print('<tr>')

if table_name == 'company_software':
    companies = software_db.select_all_from(conn, 'company')
    softwares = software_db.select_all_from(conn, 'software')
    for record in data:
        print('<tr>')
        print(f'<td>{record[0]}</td>')
        for company in companies:
            if company[0] == record[1]:
                print(f'<td>{company[1]}</td>')
        for software in softwares:
            if software[0] == record[2]:
                print(f'<td>{software[1]}</td>')
        print(f'<td><a href="/cgi-bin/table_detail.py?table={table_name}&del_line={record[0]}">удалить</a></td>')
        print('</tr>')
else:
    for record in data:
        print('<tr>')
        for obj in record:
            print(f'<td>{obj}</td>')
        print(f'<td><a href="/cgi-bin/table_detail.py?table={table_name}&del_line={record[0]}">удалить</a></td>')
        print('</tr>')

print('<tr>')
print('<td>-</td>')

print(f'<form action="/cgi-bin/table_detail.py?table={table_name}&last_row={data[len(data) - 1][0]}" method="POST">')
if table_name == 'company_software':
    tags = software_db.en_columns[table_name]

    print(f'<td><select name={tags[1]}>')
    for user in software_db.select_all_from(conn, 'company'):
        print(f'<option value="{user[0]}">{user[1]}</option>')
    print('</select></td>')

    print(f'<td><select name={tags[2]}>')
    for elec in software_db.select_all_from(conn, 'software'):
        print(f'<option value="{elec[0]}">{elec[1]}</option>')
    print('</select></td>')
else:
    for tag in software_db.en_columns[table_name]:
        if tag == 'ID': continue
        print(f'<td><input type="text" name="{tag}" /></td>')
print(f'<td><button type="submit">добавить</button></td>')
print('</form>')

print('</tr>')

print('</table>')

print(f'<a href="/cgi-bin/index.py">На главную</a>')

conn.close()