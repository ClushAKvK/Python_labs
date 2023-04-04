from http.server import HTTPServer, CGIHTTPRequestHandler
import dbmusic
from Saska.task4 import xmlmusic


def main():
    conn = dbmusic.open_connection()
    dbmusic.create_entities(conn)
    dbmusic.insert_data(conn)
    conn.close()

    xmlmusic.create_xml()

    server_address = ("", 8000)
    httpd = HTTPServer(server_address, CGIHTTPRequestHandler)
    httpd.serve_forever()


if __name__ == '__main__':
    main()