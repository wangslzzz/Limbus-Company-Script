import time
from PIL import Image
import pyautogui
from utils import find_image, drag, click_image
from pyautogui import ImageNotFoundException

def explore_react():
    # 把火车拖到舒适位置
    try:
        sx, sy = find_image('img/explore/exploring.png')
        drag(sx, sy, 650, 549)
    except ImageNotFoundException: pass

    # 按优先级选择下一步
    image_paths = [
        'img/icon/event_1.png',
        'img/icon/event_2.png',
        'img/icon/combat1_1.png',
        'img/icon/combat1_2.png',
        'img/icon/combat2_1.png',
        'img/icon/combat3_1.png',
        'img/icon/combat3_2.png',
        'img/icon/combat4_1.png',
        'img/icon/combat4_2.png',
        'img/icon/shop_1.png',
        'img/icon/shop_2.png',
        'img/icon/boss_combat_1.png',
    ]

    screen = pyautogui.screenshot()

    for image_path in image_paths:
        image = Image.open(image_path)

        try:
            location = pyautogui.locate(image, screen, confidence=0.8, grayscale=True)
            center = pyautogui.center(location)
            pyautogui.click(center)
            time.sleep(1)
            click_image('img/explore/enter.png')
            return
        except ImageNotFoundException: pass
        except Exception as e:
            print(f'寻路时，寻找 {image_path} 时出错：{e}')
            raise

    # 尝试点右，右上，右下
    for center in [(1020, 550), (1020, 200), (1020, 900)]:
        try:
            pyautogui.click(center)
            time.sleep(1)
            click_image('img/explore/enter.png')
            return
        except ImageNotFoundException: pass

    print('寻路失败')



def option_react():
    try:
        click_image('img/event/ego_accessory.png')
    except pyautogui.ImageNotFoundException:
        pyautogui.click(1438, 388)
    time.sleep(1)

def skip_react():
    try:
        click_image('img/event/skip.png')
        pyautogui.moveTo(800, 300)
    except pyautogui.ImageNotFoundException: pass
    try:
        click_image('img/event/skip.png')
        pyautogui.moveTo(800, 300)
    except pyautogui.ImageNotFoundException: pass