import time
import pyautogui
import pathlib
from utils import *

def assure_current_interface(image_path):
    if not is_interface(image_path):
        print(f'当前不是期望界面 {image_path}')
        raise pyautogui.ImageNotFoundException

def clear_energy():
    """清空体力"""
    assure_current_interface('img/glass_window.png')

    pyautogui.click(584, 1047)
    time.sleep(1)
    pyautogui.click(1205, 541)
    time.sleep(0.5)
    pyautogui.click(1123, 852)
    time.sleep(1)
    pyautogui.click(1564, 584)
    time.sleep(0.5)

def turn_to_interface(goal, position, interim=2, max_patience=10):
    """点击position直到进入期望界面"""
    pyautogui.click(*position)
    time.sleep(interim)

    patience = 0
    while not is_interface(goal):
        pyautogui.click(*position)
        time.sleep(interim)
        patience += 1

        if patience > max_patience:
            raise TimeoutError(f'转到界面 {goal} 超时')

def wait_until_interface(goal, max_patience=10):
    """等到进入期望界面"""
    patience = 0
    while not is_interface(goal):
        time.sleep(2)
        patience += 1
        if patience > max_patience:
            raise TimeoutError(f'等待界面 {goal} 超时')

def drag(sx, sy, ex, ey):
    pyautogui.moveTo(sx, sy)
    time.sleep(0.5)
    pyautogui.dragTo(ex, ey, duration=2, button='left')
    time.sleep(0.5)

def find_image(image_path):
    location = pyautogui.locateOnScreen(image_path, confidence=0.8, grayscale=True)
    return pyautogui.center(location)

def click_image(image_path):
    center = find_image(image_path)
    pyautogui.click(*center)
    time.sleep(0.5)

# ------------------------------------------------------------

def find_path():
    # 把火车拖到舒适位置
    sx, sy = find_image('img/exploring.png')
    drag(sx, sy, 650, 549)

    # 按优先级选择下一步
    images = [
        'img/exploring/event_1.png',
        'img/exploring/event_2.png',
        'img/exploring/event_3.png',
        'img/exploring/combat1_1.png',
        'img/exploring/combat1_2.png',
        'img/exploring/combat1_3.png',
        'img/exploring/combat2_1.png',
        'img/exploring/combat2_2.png',
        'img/exploring/combat3_1.png',
        'img/exploring/chair.png',
        'img/exploring/shop_1.png',
        'img/exploring/shop_2.png',
        'img/exploring/shop_3.png',
        'img/exploring/boss_combat_1.png',
        'img/exploring/boss_combat_2.png',
        'img/exploring/boss_combat_3.png'
    ]

    for image_path in images:
        try:
            click_image(image_path)
            try:
                click_image('img/exploring/enter.png',)
                return
            except pyautogui.ImageNotFoundException:
                continue
            except Exception as e:
                print(f"寻路时寻找确认键时出错 {image_path}: {e}")
                raise e
        except pyautogui.ImageNotFoundException:
            continue
        except Exception as e:
            print(f"寻路时寻找图标时出错 {image_path}: {e}")
            raise e

    print('寻路失败！')
    raise pyautogui.ImageNotFoundException

# ------------------------------------------------------------

def judge_react():
    if is_interface('img/combat/fighting.png'):
        # 战斗中
        time.sleep(2)

    elif is_interface('img/combat/combat_tips.png'):
        # 少女祈祷中
        time.sleep(2)

    elif is_interface('img/combat/give_command.png'):
        # P + Enter
        pyautogui.press('p')
        time.sleep(0.5)
        pyautogui.press('enter')

    elif is_interface('img/combat/precombat.png'):
        # 战前入口
        # if is_interface('img/sinner/rodya.png'):
        #     pyautogui.click(839, 711)
        #     time.sleep(0.5)
        # if is_interface('img/sinner/honglu.png'):
        #     pyautogui.click(1436, 413)
        #     time.sleep(0.5)
        # if is_interface('img/sinner/faust.png'):
        #     pyautogui.click(655, 406)
        #     time.sleep(0.5)
        # if is_interface('img/sinner/gregor.png'):
        #     pyautogui.click(1431, 720)
        #     time.sleep(0.5)

        pyautogui.click(1714, 928)

    elif is_interface('img/exploring.png'):
        # 探索中
        find_path()

    elif is_interface('img/combat/get_ego_gift.png'):
        # 确认ego饰品礼物
        pyautogui.click(960, 840)
        time.sleep(1)

    # elif is_interface('img/exploring/debuff.png'):  # incomplete: mounting trials
    #     # 选择debuff
    #
    elif is_interface('img/combat/select_reward_card.png'):
        # 选择奖励卡
        pyautogui.click(1028, 559)
        time.sleep(1)
        pyautogui.click(1213, 836)

    elif is_interface('img/combat/acquire_ego_accessory.png'):
        # 获得ego饰品
        pyautogui.click(1208, 576)
        time.sleep(1)
        pyautogui.click(1668, 915)

    elif is_interface('img/event/option.png'):
        # 做事件选择
        try:
            click_image('img/event/ego_accessory.png')
        except pyautogui.ImageNotFoundException:
            pyautogui.click(1438, 388)

    elif is_interface('img/event/continue.png'):
        # 点继续按钮
        pyautogui.click(1682, 1015)
        time.sleep(1)

    elif is_interface('img/event/judge.png'):
        # 判定无脑选君主宝
        pyautogui.click(696, 1017)
        time.sleep(1)
        pyautogui.click(1690, 1026)
        time.sleep(3)

    elif is_interface('img/event/skip.png'):
        # 点击skip
        click_image('img/event/skip.png')
        pyautogui.moveTo(700, 200)

    elif is_interface('img/shop.png'):
        # 商店
        pyautogui.click(1681, 1033)
        time.sleep(0.5)
        pyautogui.click(1147, 794)

    elif is_interface('img/choose_card_pack.png'):
        # 选卡包
        drag(sx=957, sy=566, ex=962, ey=912)
        time.sleep(2)

    # elif is_interface('img/interface/victory.png'):
    #     # 镜牢胜利

    elif is_interface('img/glass_window.png'):
        # 玻璃窗
        pyautogui.click(1318, 1016)
        time.sleep(1)

    elif is_interface('img/drivers_seat.png'):
        # 驾驶席
        pyautogui.click(652, 503)
        time.sleep(1)

    elif is_interface('img/entrance.png'):
        # 镜牢入口
        pyautogui.click(992, 582)
        time.sleep(1)
        pyautogui.click(1127, 781)
        time.sleep(1)

    elif is_interface('img/choose_team.png'):
        # 选择配队
        pyautogui.click(1718, 921)
        time.sleep(1)
        pyautogui.click(1133, 797)
        time.sleep(1)

    elif is_interface('img/starlight.png'):
        # 选择星光
        pyautogui.click(387, 428)
        time.sleep(0.5)
        pyautogui.click(971, 407)
        time.sleep(0.5)
        pyautogui.click(1292, 411)
        time.sleep(0.5)
        pyautogui.click(1523, 400)
        time.sleep(0.5)
        pyautogui.click(1784, 1073)
        time.sleep(0.5)
        pyautogui.click(1113, 845)
        time.sleep(1)

    elif is_interface('img/choose_ego_accessory.png'):
        # 选择ego饰品
        pyautogui.click(981, 436)
        time.sleep(0.5)
        pyautogui.click(1503, 461)
        time.sleep(0.5)
        pyautogui.click(1436, 610)
        time.sleep(0.5)
        pyautogui.click(1607, 933)
        time.sleep(1)
    else:
        print('识别失败')