import xml.etree.ElementTree as ET

from Saska.task4 import dbmusic

entities = ['user', 'track', 'user_playlist', 'album']

tags = {
    'user' : ['userId', 'firstName', 'lastName', 'playlistSize'],
    'track': ['trackId', 'albumId', 'title', 'singer', 'duration'],
    'user_playlist': ['userPlaylistId', 'userId', 'trackId'],
    'album': ['albumId', 'title', 'description', 'pubDate']
}


def create_xml():

    conn = dbmusic.open_connection()

    root = ET.Element('entities')
    # tree = ET.ElementTree()

    for i, entity in enumerate(entities):

        ent = ET.Element('entity')
        root.append(ent)

        data = dbmusic.get_all_from(conn, entity)
        for record in data:
            config = ET.Element(entity)
            config = ET.SubElement(config, entity)
            ent.append(config)
            for idx, tag in enumerate(tags[entity]):
                rec = ET.SubElement(config, tag)
                rec.text = str(record[idx])

    tree = ET.ElementTree(root)

    tree.write(f"Output.xml", encoding='utf-8', xml_declaration=True)