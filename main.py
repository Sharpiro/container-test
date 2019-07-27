import os
port = os.getenv("PORT")
port = int(port) if port != None else 8000
print(port)

import http.server
import socketserver

PORT = port

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()
