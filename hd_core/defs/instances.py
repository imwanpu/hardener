"""
单例
"""

from classes import HardenItem
from enums import EnumForSystem, EnumForIsNeedReboot


# 加固项表，手动维护
# TODO 写加固项表，之前先写类
#

# key 为 HardenItem 的 id 属性，手动维护此表
# 
table_of_harden_items: dict[str, HardenItem] = {
    'STG-0001': HardenItem(
        id='STG-0001-CE7',
        description='helloword时间测试',
        target_system=EnumForSystem.CENTOS7,
        is_need_reboot=EnumForIsNeedReboot.NO
    ),
}


