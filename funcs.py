"""
    一些与业务逻辑相关性较小的工具函数
"""

from typing import List
from csv import reader

def csv2matrix(path) -> List[List[str]]:
    matrix = []
    with open(path, newline='', encoding='utf-8') as csvfile:
        for row in reader(csvfile):
            matrix.append([])
            for element in row:
                matrix[-1].append(element)
    return [row for row in matrix if len(row) != 0]
