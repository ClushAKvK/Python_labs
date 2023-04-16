from http.server import HTTPServer, CGIHTTPRequestHandler

import electronicdb
import electronicxml

def main():
    # conn = electronicdb.open_connection()
    # electronicdb.create_entities(conn)
    # electronicdb.insert_data(conn)
    # conn.close()
    #
    electronicxml.create_xml()

    # server_address = ("", 8000)
    # httpd = HTTPServer(server_address, CGIHTTPRequestHandler)
    # httpd.serve_forever()


if __name__ == '__main__':
    main()