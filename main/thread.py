import threading


class Thread(threading.Thread):
  def __init__(self, info, handle):
    threading.Thread.__init__(self)
    self.info = info
    self.handle = handle
  def run(self):
    self.handle(self.info)
