from game_states import *
from utils import click_top, real_len

states = [
    comb_1, # 战斗中
    loa_1,  # 少女祈祷中
    comb_2, # 下达指令
    exp_1,  # 探索中
    eve_1,  # 选择选项
    eve_2,  # 点继续按钮
    eve_3,  # 事件判定
    eve_4,  # 点继续按钮
    oth_1,  # 未领取奖励
    comb_4, # 获得ego饰品奖励
    comb_5, # 挑选奖励卡
    exp_2,  # 商店
    exp_3,  # 选择卡包
    comb_6, # 选择卡包
    out_1,  # 玻璃窗
    out_2,  # 驾驶席
    pre_1,  # 镜牢入口
    pre_2,  # 选择镜牢队伍
    comb_7, # 战前准备但未选择人格
    comb_3, # 战前准备
    pre_3,  # 选择星光
    pre_4,  # 选择镜牢入口ego饰品
    exp_4,  # 镜牢胜利
    oth_2,  # 选择人格
]


def judge_react():
    pyautogui.moveTo(1000, 10)
    screen = pyautogui.screenshot()
    for state in states:
        if state.condition(screen=screen) and state.condition():
            state.action()
            return state


def play_game(react_times=2500):
    print('======== 开始运行 ========')
    click_top()

    start_time = time.time()
    last_time = start_time
    log = []

    for i in range(react_times):
        state = judge_react()
        complete_time = time.time()
        run_time = complete_time - last_time
        info = state.name if state else '判断失败'
        log.append((info, run_time))
        last_time = complete_time

        if state == exp_4: break # 胜利

        if i % 10 == 0:
            print(f'{info + " " * (20 - real_len(info))} |   run time: {run_time:.3f}s')

    print('======== 运行结束 ========\n')

    end_time = time.time()
    total_time = round(end_time - start_time)

    data = {}
    for info, run_time in log:
        if info in data: data[info].append(run_time)
        else : data[info] = [run_time]

    print('数据总结：')
    print(f'- 总共反应次数：{len(log)}')
    print(f'- 总共运行时间：{total_time}s\n')
    print('各界面类型出现次数：')
    for info in data:
        acc = len(data[info])
        avg = sum(data[info]) / acc
        print(f'- {info}：出现 {acc} 次，平均反应时间 {avg:.3f}s')
    print()

# -----------------------------------------------------------------------------

if __name__ == '__main__':
    play_game()