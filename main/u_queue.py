# -*- coding: UTF-8 -*-

import u_time as Time
import queue

class Queue():
  def __init__(self, queue_size = 0):
    self.__queue = queue.Queue(queue_size)
    self.__queue_lock_status = False
  
  def push(self, content, delay_time = 0):
    if delay_time > 0:
      Time.Sleep(delay_time)
      self.__queue.put(content)
    else:
      self.__queue.put_nowait(content)

  def pop(self):
    if not self.isEmpty():
      return self.__queue.get()
    raise Exception('Queue 已经为空......')

  def size(self):
    return self.__queue.qsize()

  def isEmpty(self):
    return self.__queue.empty()
  
  def isFull(self):
    return self.__queue.full()

  def pause(self):
    if self.__queue_lock_status:
      return
    self.__queue_lock_status = True
    self.__queue.join()
  
  def endPause(self):
    if not self.__queue_lock_status:
      return
    self.__queue_lock_status = False
    self.__queue.task_done()


# q = Queue()
# q.push(1, 1)
# print(q.size())
# q.push(2, 2)
# print(q.size())
# q.push(3, 3)
# print(q.size())
# print(q, q.size(), q.pop(), q.pop(), q.pop(), q.size())
