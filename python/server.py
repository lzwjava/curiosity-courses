class BaseHandler:
  def handle(self, request:str):
    pass

class Server:
  def __init__(self, handlerClass):
    self.handlerClass = handlerClass

  def run(self):    
    while True:
      request = input()
      self.handlerClass().handle(request)
