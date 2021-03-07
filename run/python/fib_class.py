from fib import f

class BaseHandler:
  def handle(n:int) -> int:
    return 0

class Handler(BaseHandler):
  def handle(n):
    return f(n)

class Server():
  def __init__(self, handlerClass):
    self.handlerClass = handlerClass

  def run(self):
    while True:
      n = input("n:")
      n = int(n)
      self.handlerClass().handle(n)

server = Server(Handler)
server.run()
