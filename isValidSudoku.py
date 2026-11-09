# class Solution:

#     def isValidSudoku(self, board: List[List[str]]) -> bool:
#         pass

import math

def remove_points(lst: list):

    return [l for l in lst if l != '.']

def isDuplicated(lst):

    return len(lst) != len(set(lst))

def inverseMatrix(lsts: list[list[str]]):

    result = []

    for i in range(len(lsts)):
        result.append([])

    for i, lst in enumerate(lsts):
        for j, l in enumerate(lst):
            result[j].append(l)


    return result

def sublsts(lsts: list[list[str]]):

    lent = int(math.sqrt(len(lsts)))


    result = []

    for i in range(lent):
        result.append([])

    for k in range(lent):

        for i in range(lent):
            for j in range




board = [
    ["1","2",".",".","3",".",".",".","."],
    ["4",".",".","5",".",".",".",".","."],
    [".","9","8",".",".",".",".",".","3"],
    ["5",".",".",".","6",".",".",".","4"],
    [".",".",".","8",".","3",".",".","5"],
    ["7",".",".",".","2",".",".",".","6"],
    [".",".",".",".",".",".","2",".","."],
    [".",".",".","4","1","9",".",".","8"],
    [".",".",".",".","8",".",".","7","9"]
]


print(sublsts(board))