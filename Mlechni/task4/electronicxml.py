import xml.etree.ElementTree as ET

import electronicdb

entities = ['user', 'electronic', 'basket']

tags = {
    'user': ['userId', 'firstName', 'lastName'],
    'electronic': ['electronicId', 'title', 'manufacturer', 'price'],
    'basket': ['basketId', 'userId', 'electronicId']
}


def create_xml():

    conn = electronicdb.open_connection()

    root = ET.Element('entities')
    # tree = ET.ElementTree()

    for i, entity in enumerate(entities):

        ent = ET.Element('entity')
        root.append(ent)

        data = electronicdb.select_all_from(conn, entity)
        for record in data:
            config = ET.Element(entity)
            config = ET.SubElement(config, entity)
            ent.append(config)
            for idx, tag in enumerate(tags[entity]):
                rec = ET.SubElement(config, tag)
                rec.text = str(record[idx])

    tree = ET.ElementTree(root)

    tree.write(f"electronic.xml", encoding='utf-8', xml_declaration=True)