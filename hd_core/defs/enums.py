from enum import Enum, unique


@unique
class EnumForSystem(Enum):
    # 信息获取方法：`cat /etc/os-release | grep PRETTY_NAME | awk -F "=" '{ print $2}' | awk -F "\"" '{ print $2 }'`
    # UBUNTU2004 = "Ubuntu 20.04"  #TODO 待适配 Ubuntu 20.04
    CENTOS7 = "CentOS Linux 7 (Core)"
    # ROCKY8="" #TODO 待适配 Rocky 8
    # DEBIAN12="Debian GNU/Linux 12 (bookworm)" #TODO 待适配 Debian 12


@unique
class EnumForIsNeedReboot(Enum):
    YES = "Yes"
    NO = "No"


@unique
class EnumForResoultOfExecutedCommand(Enum):
    SUCCESS = "Success"
    FAILURE = "Failure"
