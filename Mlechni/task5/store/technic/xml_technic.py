import xml.etree.ElementTree as ET
from .managedb import select_all_from

entities = ['user', 'electronic', 'basket']

tags = {
    'user' : ['userId', 'name', 'slogan'],
    'electronic': ['electronicId', 'name', 'description'],
    'basket': ['userSymptomId', 'userId', 'electronicId']
}


def record_val(record):
    for val in record.values():
        yield str(val)


def create_xml(models):

    root = ET.Element('entities')
    # tree = ET.ElementTree()

    for i, model in enumerate(models):

        ent = ET.Element('entity')
        root.append(ent)

        data = select_all_from(model)
        for record in data:
            config = ET.Element(model._meta.model_name)
            config = ET.SubElement(config, model._meta.model_name)
            ent.append(config)
            for tag, val in zip(tags[model._meta.model_name], record.values()):
                rec = ET.SubElement(config, tag)
                rec.text = str(val)

    tree = ET.ElementTree(root)

    tree.write(f"Technic.xml", encoding='utf-8', xml_declaration=True)