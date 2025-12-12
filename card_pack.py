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

c1 = CardPack(name='WARP快车谋杀案',  image_path='img/card_pack/1.png',  priority=5)
c2 = CardPack(name='伏行深渊',        image_path='img/card_pack/2.png',  priority=3)
c3 = CardPack(name='落泪者们',        image_path='img/card_pack/3.png',  priority=3)
c4 = CardPack(name='钉与锤',         image_path='img/card_pack/4.png',   priority=3)
c5 = CardPack(name='无慈悲者',        image_path='img/card_pack/5.png',  priority=4)
c6 = CardPack(name='自动工厂',        image_path='img/card_pack/6.png',  priority=4)
c7 = CardPack(name='巢、工厂、技术',   image_path='img/card_pack/7.png',  priority=3)
c8 = CardPack(name='身无分文的赌徒',   image_path='img/card_pack/8.png',  priority=2)
c9 = CardPack(name='无归属者',        image_path='img/card_pack/9.png',  priority=1)
c10 = CardPack(name='信仰与侵蚀',     image_path='img/card_pack/10.png', priority=2)
c11 = CardPack(name='被遗忘者们',     image_path='img/card_pack/11.png', priority=2)
c12 = CardPack(name='当斩之物',       image_path='img/card_pack/12.png', priority=2)
c13 = CardPack(name='湖的世界',       image_path='img/card_pack/13.png', priority=3)
c14 = CardPack(name='当贯之物',       image_path='img/card_pack/14.png', priority=2)
c15 = CardPack(name='地狱鸡',        image_path='img/card_pack/15.png',  priority=1)
c16 = CardPack(name='因情感困惑者',    image_path='img/card_pack/16.png', priority=2)
c17 = CardPack(name='被情感批判者',    image_path='img/card_pack/17.png', priority=3)
c18 = CardPack(name='憎恶与绝望',     image_path='img/card_pack/18.png',  priority=5)
c19 = CardPack(name='宅邸的副产物',    image_path='img/card_pack/19.png', priority=4)
c20 = CardPack(name='紫罗兰的正午',    image_path='img/card_pack/20.png', priority=4)
c21 = CardPack(name='虚张声势的傲慢',  image_path='img/card_pack/21.png',  priority=4)
c22 = CardPack(name='由子弹刻下的句点', image_path='img/card_pack/22.png', priority=5)
c23 = CardPack(name='20区的奇迹',     image_path='img/card_pack/23.png', priority=3)
c24 = CardPack(name='肉斩骨断',       image_path='img/card_pack/24.png', priority=3)
c25 = CardPack(name='切磋琢春',       image_path='img/card_pack/25.png', priority=5)
c26 = CardPack(name='某个世界',       image_path='img/card_pack/26.png', priority=4)
c27 = CardPack(name='深夜清扫',       image_path='img/card_pack/27.png', priority=5)
c28 = CardPack(name='去海边',        image_path='img/card_pack/28.png',  priority=4)
c29 = CardPack(name='受情感压迫者',    image_path='img/card_pack/29.png', priority=2)
c30 = CardPack(name='于情感沉溺者',    image_path='img/card_pack/30.png', priority=4)
c31 = CardPack(name='落花',          image_path='img/card_pack/31.png', priority=3)
c32 = CardPack(name='当碎之物',       image_path='img/card_pack/32.png', priority=3)
c33 = CardPack(name='寒微的嫉妒',     image_path='img/card_pack/33.png',  priority=3)
c34 = CardPack(name='堕落的忧郁',     image_path='img/card_pack/34.png',  priority=2)
c35 = CardPack(name='吞噬的暴食',     image_path='img/card_pack/35.png',  priority=2)
c36 = CardPack(name='LCB定期体检',   image_path='img/card_pack/36.png',  priority=5)
c37 = CardPack(name='穿刺者们',      image_path='img/card_pack/37.png',  priority=4)
c38 = CardPack(name='压抑的暴怒',     image_path='img/card_pack/38.png',  priority=4)
c39 = CardPack(name='沉迷的色欲',     image_path='img/card_pack/39.png',  priority=2)
c40 = CardPack(name='空转的怠惰',     image_path='img/card_pack/40.png',  priority=4)
c41 = CardPack(name='斩切者们',     image_path='img/card_pack/41.png',  priority=3)


all_card_packs = [c1, c2, c3, c4, c5, c6, c7, c8, c9, c10,
                  c11, c12, c13, c14, c15, c16, c17, c18, c19, c20,
                  c21, c22, c23, c24, c25, c26, c27, c28, c29, c30,
                  c31, c32, c33, c34, c35, c36, c37, c38, c39, c40,
                  c41]

# -----------------------------------------------------------------------------

def identify(image, pos):
    for candidate in all_card_packs:
        candidate_image = Image.open(candidate.image_path)
        try:
            pyautogui.locate(image, candidate_image, confidence=0.85, grayscale=True)
            return candidate
        except pyautogui.ImageNotFoundException: pass
    raise RuntimeError(f'图片识别失败, pos={pos}')


def _drag_card_pack(card_pack, pos):
    print(f'选择卡包：{card_pack.name}')
    if pos == 1: drag(641, 560, 639, 941)
    elif pos == 2: drag(957, 566, 962, 912)
    elif pos == 3: drag(1272, 591, 1277, 946)
    time.sleep(5)


def _choose_card_pack(have_to_choose_one=False):
    card_packs = []

    for pos in range(1, 4):
        if pos == 1: lx, ly, rx, ry = 520, 357, 753, 817
        elif pos == 2: lx, ly, rx, ry = 841, 355, 1067, 818
        elif pos == 3: lx, ly, rx, ry = 1151, 352, 1384, 819
        width, height = rx - lx, ry - ly
        image = pyautogui.screenshot(region=(lx, ly, width, height))

        card_pack = identify(image, pos)
        card_packs.append(card_pack)

    print(f'卡包：{', '.join([card_pack.name for card_pack in card_packs])}')

    i, card_pack = min(enumerate(card_packs), key=lambda x: x[1].priority)
    if card_pack.priority <= 2 or have_to_choose_one:
        _drag_card_pack(card_pack, pos=i+1)
        return True

    return False


def choose_card_pack():
    time.sleep(2) # 卡包会晃一下
    try :
        res = _choose_card_pack()
    except RuntimeError as e:
        print(f'识别卡包时出现异常：{e}')
        return

    if not res:
        print('刷新')
        pyautogui.click(1624, 112)
        time.sleep(3)
        try:
            _choose_card_pack(have_to_choose_one=True)
        except RuntimeError as e:
            print(f'识别卡包时出现异常：{e}')
            return