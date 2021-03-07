from http.server import SimpleHTTPRequestHandler, HTTPServer
from fib import f
from urllib.parse import urlparse,parse_qs

class Handler(SimpleHTTPRequestHandler):
    def do_GET(self):
      self.send_response(200)
      self.send_header('Content-type', 'text')      
      self.end_headers()
      parsed = urlparse(self.path)      
      qs = parse_qs(parsed.query)      
      result = ""
      if len(qs) > 0:
        ns = qs['n']
        if len(ns) > 0:          
          n = int(ns[0])
          result = str(f(n))
      self.wfile.write(bytes(result, "utf-8"))
      self.wfile.write(bytes(result, "utf-8"))

server = HTTPServer(("127.0.0.1", 8000), Handler)

server.serve_forever()

