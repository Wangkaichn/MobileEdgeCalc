# mp: MEC Server Producer
# 产生 MEC 服务器资源

import math, random
import u_mysql as Mysql

Max_Point_X = 500             # MEC Server 的最大 X 值
Max_Point_Y = 500             # MEC Server 的最大 Y 值
Kccf_Scope_Of_MEC = [         # MEC Server 的时钟频率所有取值
  1.5 * math.pow(10, 6),
  2.5 * math.pow(10, 6),
  3.0 * math.pow(10, 6),
]                             
Min_Thread_ID_Of_MEC = 1000   # MEC Server 的最小 Port
Host_Scope_Of_MEC = [         # MEC Server 的 Host 所有取值
  '192.168.1.104',
  '192.168.1.105',
  '192.168.1.106',
  '192.168.1.107',
]
Port_Of_MEC = 8000            # MEC Server 的 Port

def CreateSingleMECSercer():
  current_x = random.randint(0, Max_Point_X)
  current_y = random.randint(0, Max_Point_Y)
  current_Kccf_index = random.randint(0, 2)
  current_Kccf = int(Kccf_Scope_Of_MEC[current_Kccf_index])
  return (current_x, current_y, current_Kccf)

def CreateMultipleMECSercer(mec_count = 1):
  multiple_mec_server = []
  mec_count = int(mec_count)
  for _ in range(mec_count):
    single_mec_server = CreateSingleMECSercer()
    multiple_mec_server.append(single_mec_server)
  return multiple_mec_server

def get_host_of_mec(current_mec_index, mec_total_count):
  allowed_host_count = len(Host_Scope_Of_MEC)
  interval = mec_total_count / allowed_host_count
  host_index = math.floor(current_mec_index / interval)
  host = repr(Host_Scope_Of_MEC[host_index])
  return host

def SaveServerToDataBase(mec_arrow = []):
  mec_count = len(mec_arrow)
  db, cursor = Mysql.get_handle()
  for index in range(mec_count):
    current_mec = mec_arrow[index - 1]
    x, y, Kccf = current_mec
    host = get_host_of_mec(index, mec_count)
    thread_id = Min_Thread_ID_Of_MEC + index
    sql = """INSERT INTO mec_info
            (x, y, Kccf, status, host, port, thread_id)
            VALUES (%s, %s, %s, %d, %s, %s, 'thread_id_%s')
          """ % (x, y, Kccf, 0, host, Port_Of_MEC, thread_id)
    Mysql.execute_sql(db, cursor, sql)
  Mysql.close(db)
  print('已保存 MEC 服务器信息......')

