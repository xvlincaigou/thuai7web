from http.server import BaseHTTPRequestHandler, HTTPServer
import cgi
import sqlite3
import json

class RequestHandler(BaseHTTPRequestHandler):

    def do_OPTIONS(self):
        self.send_response(200, "ok")
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()

    def do_POST(self):
        if self.path == '/register':
            ctype, pdict = cgi.parse_header(self.headers.get('content-type'))
            if ctype == 'application/json':
                length = int(self.headers.get('content-length'))
                message = json.loads(self.rfile.read(length))
                code = message['code']
                name = message['name']
                password = message['password']

                conn = sqlite3.connect('userDB.db')
                c = conn.cursor()
                c.execute("SELECT * FROM Users WHERE code = ?", (code,))
                if c.fetchone() is not None:
                    self.send_response(400)
                    self.end_headers()
                else:
                    c.execute("INSERT INTO Users (code, name, password) VALUES (?, ?, ?)", (code, name, password))
                    conn.commit()
                    self.send_response(200)
                    self.end_headers()
                conn.close()
            else:
                self.send_response(400)
                self.end_headers()
        else:
            self.send_response(404)
            self.end_headers()
    
    def do_GET(self):
        self.send_response(200)
        self.end_headers()

def run(server_class=HTTPServer, handler_class=RequestHandler):
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()

run()