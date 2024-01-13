import platform

from hd_core import setting


def test_shell_script_dir():
    # 此处仅判断是否为 Windows，后面需要判断是 MacOS 和 Linux 的时候再加
    if platform.system() == "Windows":
        assert (
            setting.shell_script_dir.casefold()
            == "c:\\Users\huber\\Documents\\hardener\\hd_core\\shell_scripts\\".casefold()
        )
