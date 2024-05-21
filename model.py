from concurrent.futures import ThreadPoolExecutor
from typing import List

from defs import Host
from funcs import csv2matrix
from metaInfo import indexPath, hostsPath

hosts: List[Host] = []
needReboot = False
# indexOfscriptNeedRun: List[int] = [] # 所需执行脚本的索引
# scriptsNeedRun: List[str] = [] # 存储脚本的名字


indexMatrix: List[List] = [row for row in csv2matrix(indexPath) if row.append("不执行") == None]
hostsMatrix: List[List] = csv2matrix(hostsPath)

