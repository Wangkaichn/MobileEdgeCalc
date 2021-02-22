import threading


class _Thread(threading.Thread):
  def __init__(self, info, handle):
    threading.Thread.__init__(self)
    self.info = info
    self.handle = handle
  def run(self):
    self.handle(self.info)

class ThreadPool:
  def __init__(self):
    self._threads_info = []       # 线程信息
    self._threads_handle = []     # 线程具柄

  def _CreateSingleThread(self, info, handle):
    _thread = _Thread(info, handle)
    self._threads_info.append(info)
    self._threads_handle.append(_thread)
    return _thread

  def CreateMultipleThread(self, thread_info_arrow):
    for single_thread_info in thread_info_arrow:
      info, handle = single_thread_info
      self._CreateSingleThread(info, handle)

  def StartAllThreads(self):
    for single_thread in self._threads_handle:
      single_thread.start()
      single_thread.join()

# def p(info):
#   f = 0
#   while f < 10:
#     print('------: ', info)
#     f += 1
#     time.sleep(2)

# s = [(1, p), (2, p), (3, p)]
# tp = ThreadPool()
# tp.CreateMultipleThread(s)
# tp.StartAllThreads()
