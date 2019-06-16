from http.server import HTTPServer, BaseHTTPRequestHandler
from measurementsjson import measurements_json

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(measurements_json().encode('utf-8'))

def run_server():
    httpd = HTTPServer(('192.168.10.121', 8000), SimpleHTTPRequestHandler)
    print('Server Started')
    httpd.serve_forever()
