from ....hd_core.defs.EnumSystem import EnumSystem


class TestEnumSystem:
    def test_system_name(self):
        assert EnumSystem.centos8.name == "centos8"
