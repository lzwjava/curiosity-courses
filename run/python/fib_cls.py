from fib import f

class BaseHandler:
  def handle(self, request:str):
    pass

class FibHandler(BaseHandler):
  def handle(self, request:str):
    n = int(request)
    print('f(n)=', f(n))
    pass

class Server:
  def __init__(self, handlerClass):
    self.handlerClass = handlerClass

  def run(self):    
    while True:
      request = input()
      self.handlerClass().handle(request)

      
server = Server(FibHandler)
server.run()
