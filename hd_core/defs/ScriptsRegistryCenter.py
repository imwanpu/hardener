"""
单例模式, 是 ../shell_scripts 下脚本的抽象
"""
from .. import scripts_dir

class ScriptsRegistryCenter():
    pass

class Script():
    """
        单条命令的映射
    """
    scripts_path = scripts_dir
    def __init__(self, script_name:str, is_reboot: bool) -> None:
        self.script_path = f"{Script.scripts_path}/{script_name}"
        self.is_reboot = is_reboot
        
        
