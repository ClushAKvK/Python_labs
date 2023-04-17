from http.server import HTTPServer, CGIHTTPRequestHandler

import software_db


def main():
    # conn = software_db.open_connection()
    # software_db.create_entities(conn)
    # software_db.insert_data(conn)
    # conn.close()
    #
    # electronicxml.create_xml()

    server_address = ("", 8000)
    httpd = HTTPServer(server_address, CGIHTTPRequestHandler)
    httpd.serve_forever()


if __name__ == '__main__':
    main()