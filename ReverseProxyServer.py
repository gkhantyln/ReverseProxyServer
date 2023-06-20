import sys
import http.server
import requests
import argparse
import socketserver


class ProxyHTTPRequestHandler(http.server.BaseHTTPRequestHandler):
    protocol_version = 'HTTP/1.0'
    
    def do_HEAD(self):
        self.do_GET(body=False)
    
    def do_GET(self, body=True):
        try:
            url = f'https://{self.server.hostname}{self.path}'
            req_header = self.parse_headers()

            resp = requests.get(url, headers=req_header, verify=False)

            self.send_response(resp.status_code)
            self.send_resp_headers(resp)
            
            if body:
                self.wfile.write(resp.content)
        
        except requests.RequestException as e:
            self.send_error(500, str(e))
        
    def do_POST(self, body=True):
        try:
            url = f'https://{self.server.hostname}{self.path}'
            content_len = int(self.headers.get('content-length', 0))
            post_body = self.rfile.read(content_len)
            req_header = self.parse_headers()

            resp = requests.post(url, data=post_body, headers=req_header, verify=False)

            self.send_response(resp.status_code)
            self.send_resp_headers(resp)

            if body:
                self.wfile.write(resp.content)
        
        except requests.RequestException as e:
            self.send_error(500, str(e))
    
    def parse_headers(self):
        req_header = {}
        for line in self.headers:
            line_parts = [o.strip() for o in line.split(':', 1)]
            if len(line_parts) == 2:
                req_header[line_parts[0]] = line_parts[1]
        return req_header
    
    def send_resp_headers(self, resp):
        resp_headers = resp.headers
        for key, value in resp_headers.items():
            if key.lower() not in ['content-encoding', 'transfer-encoding', 'content-length']:
                self.send_header(key, value)
        
        self.send_header('Content-Length', str(len(resp.content)))
        self.end_headers()


class ThreadedHTTPServer(socketserver.ThreadingMixIn, http.server.HTTPServer):
    pass


def main():
    args = parse_args()
    hostname = args.hostname
    
    print(f'HTTP server is starting on {args.hostname} port {args.port}...')
    
    server_address = ('127.0.0.1', args.port)
    httpd = ThreadedHTTPServer(server_address, ProxyHTTPRequestHandler)
    httpd.hostname = hostname
    
    print('HTTP server is running as a reverse proxy')
    httpd.serve_forever()


def parse_args():
    default_hostname=input("Add Your Default Host Name >>> ")
    parser = argparse.ArgumentParser(description='Proxy HTTP requests')
    parser.add_argument('--port', dest='port', type=int, default=9999,
                        help=f'serve HTTP requests on specified port (default: random)')
    parser.add_argument('--hostname', dest='hostname', type=str, default=default_hostname,
                        help='hostname to be processed (default: {default_hostname})')
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    main()
