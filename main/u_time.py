import time

def GetLocalTime():
  local_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
  local_time_str = repr(local_time)
  return local_time_str

def Sleep(sleep_time):
  time.sleep(sleep_time)
    