"""

"""


class SetOfHardenItems:
    def __init__(self) -> None:
        self.harden_items = []

    def get_table_of_harden_items(self):
        """
        返回加固项列表，按加固项、目标系统分行
        """
        pass


class TableOfHardenItems:
    """
    根据 `set_of_harden_items` 类的实例生成。
    不要手动生成。
    """

    def __init__(self) -> None:
        self.header = ["item_id", "target_system", "shell_script", "is_need_reboot"]


class TargetHost:
    def __init__(self, address_ipv4:str=None, username:str=None, password:str=None) -> None:
        self.address_ipv4 = address_ipv4
        self.username = username
        self.password = password
        # self.private_key=None #TODO 支持密钥远程执行
