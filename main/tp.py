# TP: Task Producer
# 用户模拟移动端产生计算任务

import math, random, mysql

Max_Point_X = 500                           # 终端的最大 X 值
Max_Point_Y = 500                           # 终端的最大 Y 值
Min_Dccc_Of_Task = math.pow(10, 4)          # 任务所需的最 小 时钟频率
Max_Dccc_Of_Task = math.pow(10, 6)          # 任务所需的最 大 时钟频率
Min_Dv_Of_Task = 9 * math.pow(10, 4)        # 任务所占用的最 小 内存大小
Max_Dv_Of_Task = 5 * math.pow(10, 6)        # 任务所占用的最 大 内存大小
# 初始化任务时没有固定任务 QoS 分布
# QoS_Scope_Of_Task = [3,3,4]                 # 任务的 QoS 范围
Delay_Time_Scope_Of_Task = [1.4, 2.0, 2.4]  # 任务的可以容忍的最大时延基数

def CreateSingleTask():
  current_x = random.randint(0, Max_Point_X)
  current_y = random.randint(0, Max_Point_Y)
  current_Dccc = random.randint(Min_Dccc_Of_Task, Max_Dccc_Of_Task)
  current_Dv = random.randint(Min_Dv_Of_Task, Max_Dv_Of_Task)
  current_QoS = random.randint(1, 3)
  current_Allowed_Delay_Time_index = current_QoS - 1
  current_Allowed_Delay_Time = Delay_Time_Scope_Of_Task[current_Allowed_Delay_Time_index]
  current_Rondom_Delay_Time = round((random.random() - 0.5) / 2, 3)
  current_Allowed_Delay_Time = current_Allowed_Delay_Time + current_Rondom_Delay_Time
  return (current_x, current_y, current_Dccc, current_Dv, current_QoS, current_Allowed_Delay_Time)

def get_QoS(task_arrow):
  return task_arrow[4]

def CreateMultipleTask(task_count = 1, sorted = True):
  multiple_task = []
  for index in range(task_count):
    single_task = CreateSingleTask()
    multiple_task.append(single_task)
  if sorted:
    multiple_task.sort(key = get_QoS)
  return multiple_task

def SaveTasksToDataBase(task_arrow = []):
  db, cursor = mysql.get_handle()
  for current_task in task_arrow:
    sql = """INSERT INTO task_info
          (x, y, Dccc, Dv, QoS, MaxDelayTime)
          VALUES (%s, %s, %s, %s, %d, %s)""" % current_task
    mysql.insert(db, cursor, sql)
  mysql.close(db)
  print('已保存任务信息......')

