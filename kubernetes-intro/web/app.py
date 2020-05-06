import socketserver
import http.server
import os

PORT = int(os.environ["PORT"])
DIRECTORY = os.environ["DIRECTORY"]

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)


with socketserver.TCPServer(("", PORT), Handler) as httpd:
    httpd.serve_forever()
