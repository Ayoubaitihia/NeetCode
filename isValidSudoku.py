import math


class Solution:

    def remove_points(self, lst: list):

        return [l for l in lst if l != '.']

    def isDuplicated(self, lst):

        return len(lst) != len(set(lst))

    def inverseMatrix(self, lsts: list[list[str]]):

        result = []

        for i in range(len(lsts)):
            result.append([])

        for i, lst in enumerate(lsts):
            for j, l in enumerate(lst):
                result[j].append(l)

        return result

    def isValid(self, board: list[list[str]]) -> bool:

        for lst in board:
            if self.isDuplicated(self.remove_points(lst)):
                return False

        inverted = self.inverseMatrix(board)

        for lst in inverted:
            if self.isDuplicated(self.remove_points(lst)):
                return False

        return True


    def isValidSudoku(self, board: list[list[str]]) -> bool:

        return self.isValid(board)
            



# def sublist(lsts):

#     lent = int(math.sqrt(len(lsts)))

#     for k in range(lent):

#         chunk = [[] for _ in range(lent)]

#         for i, l in enumerate(lsts[k:lent+k]):
#                 chunk.append



board = [
    ["1","2",".",".","3",".",".",".","."],
    ["4",".",".","5",".",".",".",".","."],
    [".","9","1",".",".",".",".",".","3"],
    ["5",".",".",".","6",".",".",".","4"],
    [".",".",".","8",".","3",".",".","5"],
    ["7",".",".",".","2",".",".",".","6"],
    [".",".",".",".",".",".","2",".","."],
    [".",".",".","4","1","9",".",".","8"],
    [".",".",".",".","8",".",".","7","9"]]


sol = Solution()

print(sol.isValidSudoku(board))
