from collections.abc import Callable
from functools import partial
from card_pack import choose_card_pack
from react import *
from utils import is_interface


class State:
    def __init__(self, name, condition: Callable[[], bool], action: Callable):
        self.name = name
        self.condition = condition
        self.action = action

    def __repr__(self):
        return f'State({self.name})'


# 镜牢外

out_1 = State(
    name='玻璃窗',
    condition=partial(is_interface, image_paths='img/outside/glass_window.png'),
    action=lambda: pyautogui.click(1318, 1016)
)

out_2 = State(
    name='驾驶席',
    condition=partial(is_interface, image_paths='img/outside/drivers_seat.png'),
    action=lambda: pyautogui.click(652, 503)
)

# 准备进入

pre_1 = State(
    name='镜牢入口',
    condition=partial(is_interface, image_paths='img/prepare/entrance.png'),
    action=lambda: (
        pyautogui.click(992, 582),
        time.sleep(0.5),
        pyautogui.click(1127, 781)
    )
)

pre_2 = State(
    name='选择镜牢队伍',
    condition=partial(is_interface, image_paths='img/prepare/choose_team.png'),
    action=lambda: (
        pyautogui.click(1718, 921),
        time.sleep(0.5),
        pyautogui.click(1133, 797)
    )
)

pre_3 = State(
    name='选择星光',
    condition=partial(is_interface, image_paths='img/prepare/starlight.png'),
    action=lambda: (
        pyautogui.click(1784, 1073),
        time.sleep(0.5),
        pyautogui.click(1113, 845)
    )
)

pre_4 = State(
    name='选择镜牢入口ego饰品',
    condition=partial(is_interface, image_paths='img/prepare/choose_ego_accessory.png'),
    action=lambda: (
        pyautogui.click(989, 416),
        time.sleep(0.5),
        pyautogui.click(1495, 454),
        time.sleep(0.5),
        pyautogui.click(1590, 931)
    )
)

# 探索中

exp_1 = State(
    name='探索中',
    condition=partial(is_interface, image_paths='img/explore/exploring.png'),
    action=explore_react
)

exp_2 = State(
    name='商店',
    condition=partial(is_interface, image_paths='img/explore/in_shop.png'),
    action=lambda: (
        pyautogui.click(1681, 1033),
        time.sleep(0.5),
        pyautogui.click(1147, 794)
    )
)

exp_3 = State(
    name='选择卡包',
    condition=partial(is_interface, image_paths='img/explore/choose_card_pack.png'),
    action=choose_card_pack
)

exp_4 = State(
    name='镜牢胜利',
    condition=partial(is_interface, image_paths='img/explore/victory.png'),
    action=lambda: (
        pyautogui.click(1684, 896),
        time.sleep(1),
        pyautogui.click(1687, 960),
        time.sleep(1),
        pyautogui.click(1329, 872),
        time.sleep(1),
        pyautogui.click(1129, 796),
        time.sleep(1),
        pyautogui.click(953, 756)
    )
)

# 事件中

eve_1 = State(
    name='选择选项',
    condition=partial(is_interface, image_paths='img/event/option.png'),
    action=option_react
)

eve_2 = State(
    name='点继续按钮',
    condition=partial(is_interface, image_paths='img/event/continue.png'),
    action=lambda: pyautogui.click(1682, 1015)
)

eve_3 = State(
    name='事件判定',
    condition=partial(is_interface, image_paths='img/event/judge.png'),
    action=lambda: (
        pyautogui.click(239, 1020),
        time.sleep(0.5),
        pyautogui.click(1690, 1026)
    )
)

eve_4 = State(
    name='点skip',
    condition=partial(is_interface, image_paths='img/event/skip.png'),
    action=skip_react
)

# 战斗中

comb_1 = State(
    name='战斗中',
    condition=partial(is_interface, image_paths='img/combat/fighting.png'),
    action=lambda: time.sleep(1)
)

comb_2 = State(
    name='下达指令',
    condition=partial(is_interface, image_paths='img/combat/give_command.png'),
    action=lambda: (
        pyautogui.click(150, 100),
        pyautogui.press('p'),
        time.sleep(0.5),
        pyautogui.press('enter')
    )
)

comb_3 = State(
    name='战前准备',
    condition=partial(is_interface, image_paths='img/combat/precombat.png'),
    action=lambda: pyautogui.click(1714, 928)
)

comb_4 = State(
    name='获得ego饰品',
    condition=partial(is_interface, image_paths='img/combat/get_ego_gift.png'),
    action=lambda: pyautogui.click(960, 840)
)

comb_5 = State(
    name='选择奖励卡',
    condition=partial(is_interface, image_paths='img/combat/select_reward_card.png'),
    action=lambda: (
        pyautogui.click(1017, 561),
        time.sleep(0.5),
        pyautogui.click(1213, 836)
    )
)

comb_6 = State(
    name='获得每层结束ego饰品',
    condition=partial(is_interface, image_paths='img/combat/acquire_ego_accessory.png'),
    action=lambda: (
        pyautogui.click(1034, 610),
        time.sleep(0.5),
        pyautogui.click(1697, 917)
    )
)

comb_7 = State(
    name='战前准备但未选择人格',
    condition=partial(is_interface, image_paths='img/combat/precombat_unselected.png'),
    action=lambda: (
        pyautogui.click(837, 703),
        time.sleep(0.5),
        pyautogui.click(1437, 409),
        time.sleep(0.5),
        pyautogui.click(634, 397),
        time.sleep(0.5),
        pyautogui.click(1430, 694)
    )
)

# 加载中

loa_1 = State(
    name='少女祈祷中',
    condition=partial(is_interface, image_paths='img/loading/combat_tips.png'),
    action=lambda: time.sleep(1)
)

# 其他界面

oth_1 = State(
    name='未领取奖励',
    condition=partial(is_interface, image_paths='img/otherUI/unclaimed_reward.png'),
    action=lambda: pyautogui.click(800, 745)
)