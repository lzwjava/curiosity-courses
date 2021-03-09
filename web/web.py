from http.server import SimpleHTTPRequestHandler, HTTPServer
from fib import fplus
from urllib.parse import urlparse,parse_qs

class Handler(SimpleHTTPRequestHandler):

    def parse_n(self, s):
      parsed = urlparse(s)
      qs = parse_qs(parsed.query)
      if len(qs) > 0:
        ns = qs['n']
        if len(ns) > 0:
          n = int(ns[0])
          return n
      return None
      
    def do_GET(self):
      self.send_response(200)
      self.send_header('Content-type', 'text')
      self.end_headers()

      result = ""
      n = self.parse_n(self.path)
      if n is not None:
        result = str(fplus(n))
              
      self.wfile.write(bytes(result, "utf-8"))
      self.wfile.write(bytes(result, "utf-8"))

server = HTTPServer(("127.0.0.1", 8000), Handler)

server.serve_forever()