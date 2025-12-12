import time
import pyautogui
from PIL import Image
from utils import drag

class CardPack:
    def __init__(self, name, image_path, priority):
        self.name = name
        self.image_path = image_path
        self.priority = priority

# -----------------------------------------------------------------------------

c1 = CardPack(name='WARP快车谋杀案',  image_path='img/card_pack/1.png',  priority=5)      # 5
c2 = CardPack(name='伏行深渊',        image_path='img/card_pack/2.png',  priority=3)      # 5
c3 = CardPack(name='落泪者们',        image_path='img/card_pack/3.png',  priority=3)      # 5
c4 = CardPack(name='钉与锤',         image_path='img/card_pack/4.png',   priority=3)      # 1
c5 = CardPack(name='无慈悲者',        image_path='img/card_pack/5.png',  priority=4)      # 1
c6 = CardPack(name='自动工厂',        image_path='img/card_pack/6.png',  priority=4)      # 1, 2
c7 = CardPack(name='巢、工厂、技术',   image_path='img/card_pack/7.png',  priority=3)      # 1
c8 = CardPack(name='身无分文的赌徒',   image_path='img/card_pack/8.png',  priority=2)      # 1, 2
c9 = CardPack(name='无归属者',        image_path='img/card_pack/9.png',  priority=1)      # 1
c10 = CardPack(name='信仰与侵蚀',     image_path='img/card_pack/10.png', priority=2)      # 1
c11 = CardPack(name='被遗忘者们',     image_path='img/card_pack/11.png', priority=2)      # 1
c12 = CardPack(name='当斩之物',       image_path='img/card_pack/12.png', priority=2)      # 2
c13 = CardPack(name='湖的世界',       image_path='img/card_pack/13.png', priority=3)      # 2
c14 = CardPack(name='当贯之物',       image_path='img/card_pack/14.png', priority=2)      # 2
c15 = CardPack(name='地狱鸡',        image_path='img/card_pack/15.png',  priority=1)      # 2
c16 = CardPack(name='因情感困惑者',    image_path='img/card_pack/16.png', priority=2)      # 3
c17 = CardPack(name='被情感批判者',    image_path='img/card_pack/17.png', priority=3)      # 3
c18 = CardPack(name='憎恶与绝望',     image_path='img/card_pack/18.png',  priority=5)      # 3
c19 = CardPack(name='宅邸的副产物',    image_path='img/card_pack/19.png', priority=4)      # 3
c20 = CardPack(name='紫罗兰的正午',    image_path='img/card_pack/20.png', priority=4)      # 4
c21 = CardPack(name='虚张声势的傲慢',  image_path='img/card_pack/21.png',  priority=4)      # 4, 5
c22 = CardPack(name='由子弹刻下的句点', image_path='img/card_pack/22.png', priority=5)      # 4
c23 = CardPack(name='20区的奇迹',     image_path='img/card_pack/23.png', priority=3)      # 4
c24 = CardPack(name='肉斩骨断',       image_path='img/card_pack/24.png', priority=3)      # 4, 5
c25 = CardPack(name='切磋琢春',       image_path='img/card_pack/25.png', priority=5)      # 5
c26 = CardPack(name='某个世界',       image_path='img/card_pack/26.png', priority=4)      # 5
c27 = CardPack(name='深夜清扫',       image_path='img/card_pack/27.png', priority=5)      # 5


all_card_packs = [c1, c2, c3, c4, c5, c6, c7, c8, c9, c10,
                  c11, c12, c13, c14, c15, c16, c17, c18, c19, c20,
                  c21, c22, c23, c24, c25, c26, c27]

# -----------------------------------------------------------------------------

def identify(image):
    for candidate in all_card_packs:
        candidate_image = Image.open(candidate.image_path)
        try:
            pyautogui.locate(image, candidate_image, confidence=0.9, grayscale=True)
            return candidate
        except pyautogui.ImageNotFoundException: pass
    raise RuntimeError('图片识别失败')


def _drag_card_pack(card_pack, pos):
    print(f'选择卡包：{card_pack.name}')
    if pos == 1: drag(641, 560, 639, 941)
    elif pos == 2: drag(957, 566, 962, 912)
    elif pos == 3: drag(1272, 591, 1277, 946)
    time.sleep(5)


def _choose_card_pack(have_to_choose_one=False):
    card_packs = []

    for pos in range(1, 4):
        if pos == 1: lx, ly, rx, ry = 477, 317, 793, 855
        elif pos == 2: lx, ly, rx, ry = 798, 321, 1105, 846
        elif pos == 3: lx, ly, rx, ry = 1113, 318, 1429, 854
        width, height = rx - lx, ry - ly
        image = pyautogui.screenshot(region=(lx, ly, width, height))

        card_pack = identify(image)
        card_packs.append(card_pack)

    print(f'卡包：{', '.join([card_pack.name for card_pack in card_packs])}')

    i, card_pack = min(enumerate(card_packs), key=lambda x: x[1].priority)
    if card_pack.priority <= 2 or have_to_choose_one:
        _drag_card_pack(card_pack, pos=i+1)
        return True

    return False


def choose_card_pack():
    res = _choose_card_pack()
    if not res:
        print('刷新')
        pyautogui.click(1624, 112)
        time.sleep(3)
        _choose_card_pack(have_to_choose_one=True)