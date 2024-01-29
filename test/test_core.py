import unittest

from .test_infomation import *
from hd_core import setting


class TestFunctions(unittest.TestCase):
    pass

class TestSetting(unittest.TestCase):
    def test_shell_script_dir(self):
        self.assertEqual(
            setting.shell_script_dir.casefold(),
            "c:\\Users\huber\\Documents\\hardener\\hd_core\\shell_scripts\\".casefold()
        )