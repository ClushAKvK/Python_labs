import cgi

from Vanish.task4 import software_db, software_xml

print("Content-type: text/html; charset=utf-8")
print()

form = cgi.FieldStorage()
if form.getvalue('load_xml') == 'true':
    software_xml.create_xml()
    print('<span>База данных выгружена в XML</span>')


# print('<h2>Таблицы</h2>')
print('<table>')
print('<caption><h2>Таблицы<h2></caption>')
print('<tr>')
for en_entity, ru_entity in software_db.entities.items():
    print(f'<td><a href=/cgi-bin/table_detail.py?table={en_entity}>{ru_entity}</a></td>')
print('<tr>')
print('</table>')

print(f'''
    <a href="/cgi-bin/index.py?load_xml=true">
        <button type="submit">Выгрузить в XML</button>
    </a>
''')