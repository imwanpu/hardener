"""

"""
from enums import EnumForSystem, EnumForIsNeedReboot

class HardenItem:
    def __init__(
            self,
            id: str = None,
            description: str = None,
            target_system: EnumForSystem = None,
            shell_script: str = None,
            is_need_reboot: EnumForIsNeedReboot = None) -> None:
        self.id = id
        self.description = description
        self.target_system = target_system
        self.shell_script = shell_script
        self.is_need_reboot = is_need_reboot




class TargetHost:
    def __init__(self, address_ipv4: str = None, username: str = None, password: str = None) -> None:
        self.address_ipv4 = address_ipv4
        self.username = username
        self.password = password
        # self.private_key=None #TODO 支持密钥远程执行
