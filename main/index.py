# 初始化系统

INIT_TASK_COUNT = 100                   # 起始的任务数量
INIT_MEC_COUNT = INIT_TASK_COUNT * 1.2  # 起始的MEC数量

import tp, mp
import u_mysql as Mysql

# 1. 清空数据库
Mysql.clean_history()

# 2. 生成任务
init_task = tp.CreateMultipleTask(INIT_TASK_COUNT)
tp.SaveTasksToDataBase(init_task)

# 3. 生成 MEC
init_mec = mp.CreateMultipleMECSercer(INIT_MEC_COUNT)
mp.SaveServerToDataBase(init_mec)
