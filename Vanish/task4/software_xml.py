import xml.etree.ElementTree as ET

from Vanish.task4 import software_db

entities = ['company', 'software', 'company_software']

tags = {
    'company': ['companyId', 'name', 'slogan'],
    'software': ['softwareId', 'title', 'description', 'price'],
    'company_software': ['companySoftwareId', 'companyId', 'softwareId']
}


def create_xml():

    conn = software_db.open_connection()

    root = ET.Element('entities')
    # tree = ET.ElementTree()

    for i, entity in enumerate(entities):

        ent = ET.Element('entity')
        root.append(ent)

        data = software_db.select_all_from(conn, entity)
        for record in data:
            config = ET.Element(entity)
            config = ET.SubElement(config, entity)
            ent.append(config)
            for idx, tag in enumerate(tags[entity]):
                rec = ET.SubElement(config, tag)
                rec.text = str(record[idx])

    tree = ET.ElementTree(root)

    tree.write(f"software.xml", encoding='utf-8', xml_declaration=True)