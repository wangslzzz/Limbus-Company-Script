from utils import *
from game_states import *

def get_location():
    curx, cury = pyautogui.position()
    print(str(curx) + ', ' + str(cury))

def save_image(image_path, lx, ly, rx, ry):
    click_top()
    width, height = rx - lx, ry - ly
    region = (lx, ly, width, height)
    pyautogui.screenshot(image_path, region=region)

def getbox(image_path, lx, ly, rx, ry):
    with open('image_region.json', 'r') as f:
        data = json.load(f)
    data[image_path] = [lx, ly, rx-lx, ry-ly]
    with open('image_region.json', 'w') as f:
        json.dump(data, f, indent=4)

# click_top()
# print(comb_2.condition())
# pyautogui.locateOnScreen('img/combat/give_command.png', confidence=0.9)
get_location()

# getbox('img/combat/acquire_ego_accessory.png',
#        247, 212,
#         1736, 370
#        )

# save_image(lx=1373, ly=154, rx=1833, ry=289, image_path='img/outside/glass_window.png')

# pyautogui.screenshot('aaa.png', region=(1373,
#         154,
#         510,
#         135))

