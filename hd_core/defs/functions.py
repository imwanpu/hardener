"""

"""
import fabric

from ..setting import shell_script_dir
from .classes import TargetHost
from .enums import EnumForResoultOfExecutedCommand

def shell_file2str(shell_file_name: str) -> str:
    """
    根据文件路径获取
    """
    with open(shell_script_dir+shell_file_name,'r', encoding='utf-8') as file:
        shell_content = file.read()
    return shell_content


def run_command_to_target_host(
        target_host: TargetHost, 
        command: str) -> EnumForResoultOfExecutedCommand:
    connection = fabric.Connection(host=target_host.address_ipv4,
                               user=target_host.username,
                               connect_kwargs={'password':target_host.password})
    result = connection.run(command)
    return EnumForResoultOfExecutedCommand.SUCCESS if result.ok else EnumForResoultOfExecutedCommand.FAILURE



