# -*- coding: UTF-8 -*-

import threading


class _Built_In_Thread(threading.Thread):
  def __init__(self, info, handle):
    threading.Thread.__init__(self)
    self.info = info
    self.handle = handle
  def run(self):
    if self.info:
      self.handle(self.info)
    else:
      self.handle()

def GetAliveThreadInfo():
  return threading.enumerate()

class Thread:
  def __init__(self):
    self.__threads_info = []       # 线程信息
    self.__threads_handle = []     # 线程具柄

  def __CreateSingleThread(self, info, handle):
    thread = _Built_In_Thread(info, handle)
    self.__threads_info.append(info)
    self.__threads_handle.append(thread)
    return thread

  # thread_info_arrow ==> [(任务信息, 任务处理函数)]
  def CreateMultipleThread(self, thread_info_arrow):
    for single_thread_info in thread_info_arrow:
      info, handle = single_thread_info
      self.__CreateSingleThread(info, handle)

  def StartAllThreads(self):
    for single_thread in self.__threads_handle:
      single_thread.start()
    for single_thread in self.__threads_handle:
      single_thread.join()

  def CreateThreadLock():
    return threading.Lock()


# def p(info):
#   f = 0
#   while f < 10:
#     print('------: ', info)
#     f += 1
#     time.sleep(2)

# s = [(1, p), (2, p), (3, p)]
# tp = Thread()
# tp.CreateMultipleThread(s)
# tp.StartAllThreads()
