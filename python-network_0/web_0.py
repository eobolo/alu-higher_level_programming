from http.server import HTTPServer, BaseHTTPRequestHandler

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b'Hello Holberton School!')

if __name__ == '__main__':
    server_address = ('', 5000)
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    print('Starting server on port 5000...')
    httpd.serve_forever()
