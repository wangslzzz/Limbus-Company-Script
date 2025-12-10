import pyautogui
import json
import time

def click_top():
    pyautogui.click(957, 25)
    time.sleep(0.5)

def get_location():
    curx, cury = pyautogui.position()
    print(str(curx) + ', ' + str(cury))

def save_image(image_path, lx, ly, rx, ry):
    click_top()
    width, height = rx - lx, ry - ly
    region = (lx, ly, width, height)
    pyautogui.screenshot(image_path, region=region)

    with open('image_region.json', 'r') as f:
        data = json.load(f)
    data[image_path] = region
    with (open('image_region.json', 'w')) as f:
        json.dump(data, f, indent=4)

def is_interface(image_path, confidence=0.9):
    """
    判断是否为此界面，要求region存储在image_region.json中
    """
    with open('image_region.json', 'r') as f:
        data = json.load(f)
    region = data.get(image_path, (0, 0, 1920, 1080))

    try:
        pyautogui.locateOnScreen(image_path, region=region,
                                 confidence=confidence, grayscale=True)
        return True
    except pyautogui.ImageNotFoundException:
        return False
    except Exception as e:
        print(f"检测界面时出错 {image_path}: {e}")
        raise e
