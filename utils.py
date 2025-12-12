import json
import time
from typing import List, Union, Optional
from PIL import Image
import pyautogui
from pyautogui import ImageNotFoundException

def click_top():
    pyautogui.click(1000, 10)
    time.sleep(0.5)


def is_interface(image_paths: Union[str, List[str]],
                 screen: Optional[Image.Image] = None, confidence: float = 0.9) -> bool:
    """以寻找图标判断是否为当前界面"""
    if isinstance(image_paths, str):
        image_paths = [image_paths]

    with open('image_region.json', 'r') as f:
        data = json.load(f)

    if not screen:
        screen = pyautogui.screenshot()

    # 遍历所有图标
    for image_path in image_paths:
        image = Image.open(image_path)
        region = data.get(image_path)

        try:
            pyautogui.locate(image, screen, region=region,
                                        confidence=confidence, grayscale=True)
            return True
        except ImageNotFoundException: pass
        except Exception as e:
            print(f'判断界面时，寻找 {image_path} 时出错：{e}')
            raise

    return False


def clear_energy():
    pyautogui.click(584, 1047)
    time.sleep(0.5)
    pyautogui.click(1205, 541)
    time.sleep(0.5)
    pyautogui.click(1123, 852)
    time.sleep(0.5)
    pyautogui.click(1564, 584)


def drag(sx, sy, ex, ey):
    pyautogui.moveTo(sx, sy)
    time.sleep(0.5)
    pyautogui.dragTo(ex, ey, duration=1)


def find_image(image_path):
    with open('image_region.json', 'r') as f:
        data = json.load(f)
    region = data.get(image_path)
    location = pyautogui.locateOnScreen(image_path, region=region,
                                        confidence=0.8, grayscale=True)
    return pyautogui.center(location)


def click_image(image_path):
    center = find_image(image_path)
    pyautogui.click(*center)
    time.sleep(0.5)


def real_len(string):
    length = 0
    for char in string:
        if '\u4e00' <= char <= '\u9fff': length += 2
        else: length += 1
    return length