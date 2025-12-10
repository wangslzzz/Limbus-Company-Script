import time
from actions import *

start_time = time.time()
print('======== 开始运行 ========\n')
click_top()
while True:
    judge_react()

end_time = time.time()
run_time = end_time - start_time

print(f'运行时间：{run_time:.1f} s\n')
print('======== 运行结束 ========\n')