import pyautogui

from actions import *

if is_interface('img/combat/fighting.png'):
    # 战斗中
    pass

elif is_interface('img/combat/give_command.png'):
    # P + Enter
    click_image('img/combat/give_command.png')
    click_image('img/combat/start.png')

elif is_interface('img/combat/combat_tips.png'):
    # 少女祈祷中
    pass

elif is_interface('img/exploring.png'):
    # 探索中
    find_path()

elif is_interface('img/combat/get_ego_gift.png'):
    # 确认ego饰品礼物
    pyautogui.click(960, 840)
    time.sleep(0.5)

elif is_interface('img/exploring/debuff.png'):  # incomplete: mounting trials
    # 选择debuff
    raise pyautogui.ImageNotFoundException

elif is_interface('img/combat/select_reward_card.png'): # incomplete: selectable 0/1
    # 选择奖励卡
    raise pyautogui.ImageNotFoundException

elif is_interface('img/combat/acquire_ego_gift.png'): # incomplete: acquire ego gift
    # 选择ego饰品奖励
    raise pyautogui.ImageNotFoundException

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

elif is_interface('img/event/result.png'): # incomplete
    # 等待事件后果
    raise pyautogui.ImageNotFoundException

elif is_interface('img/event/skip.png'):
    # 点击skip
    pyautogui.click(900, 510)
    time.sleep(0.5)

elif is_interface('img/chair/chair.png'): # incomplete
    # 休息处
    raise pyautogui.ImageNotFoundException

elif is_interface('img/shop/shop.png'): # incomplete
    # 商店
    raise pyautogui.ImageNotFoundException

elif is_interface('img/combat/precombat.png') or is_interface('img/combat/precombat_2.png'):
    # 战前入口

elif is_interface('img/choose_card_pack.png'):
    # 选卡包

elif is_interface('img/interface/victory.png'):
    # 镜牢胜利

else:
    print('判断失败')
    raise pyautogui.ImageNotFoundException