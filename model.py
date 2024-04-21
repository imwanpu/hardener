from concurrent.futures import ThreadPoolExecutor
from typing import List

from defs import Host
from funcs import csv2matrix
from metaInfo import indexPath, hostsPath

hosts: List[Host] = []
needReboot = False
scriptsNeedRun: List[str] = [] # 存储脚本的名字

# 读取自 index.csv 文件, 不可变
indexMatrix: List[List] = csv2matrix(indexPath)
hostsMatrix: List[List] = csv2matrix(hostsPath)