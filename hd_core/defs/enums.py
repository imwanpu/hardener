from enum import Enum, unique


@unique
class EnumSystem(Enum):
    信息获取方法
    # ubuntu2004 = "Ubuntu 20.04"  #TODO 待适配 Ubuntu 20.04
    centos7= "CentOS Linux 7 (Core)"
    # rocky8="" #TODO 待适配 Rocky 8
    # debian12="Debian GNU/Linux 12 (bookworm)" #TODO 待适配 Debian 12

