class Solution:

    def remove_points(self, lst: list):
        return [l for l in lst if l != '.']

    def isDuplicated(self, lst):
        return len(lst) != len(set(lst))

    def isValidSudoku(self, board: list[list[str]]) -> bool:

        ColsHashMap = {}
        squaresHashMap = {}

        for i in range(len(board)):
            ColsHashMap[i] = []
            squaresHashMap[i] = []

        for i, b in enumerate(board):
            if self.isDuplicated(self.remove_points(b)):
                return False

        for i, lst in enumerate(board):
            for j, l in enumerate(lst):
                ColsHashMap[j].append(l)
                squaresHashMap[int(j/3)].append(l)

        for i in range(len(board)):
            if self.isDuplicated(self.remove_points(ColsHashMap[i])):
                return False

        for j in range(int(len(board)/3)):
            i = 0
            while i in range(len(board) * 3):
                start = i
                end = start + (len(board))
                if self.isDuplicated(self.remove_points(squaresHashMap[j][start:end])):
                    return False
                i += len(board)

        return True


board = [
    ["1","2","",".","3",".",".",".","."],
    ["4",".",".","5",".",".",".",".","."],
    [".","9","8",".",".",".",".",".","3"],
    ["5",".",".",".","6",".",".",".","4"],
    [".",".",".","8",".","3",".",".","5"],
    ["7",".",".",".","2",".",".",".","6"],
    [".",".",".",".",".",".","2",".","."],
    [".",".",".","4","1","9",".",".","8"],
    [".",".",".",".","8",".",".","7","9"]
]

sol = Solution()

print(sol.isValidSudoku(board))



# for i in range(len(board)):
#     ColsHashMap[i] = []
#     squaresHashMap[i] = []

# for i, b in enumerate(board):
#     RowsHashMap[i] = b


# for i, lst in enumerate(board):
#     for j, l in enumerate(lst):
#         ColsHashMap[j].append(l)
#         squaresHashMap[int(j/3)].append(l)


# for j in range(int(len(board)/3)):
#     i = 0
#     while i in range(len(board) * 3):
#         start = i
#         end = start + (len(board))
#         print(squaresHashMap[j][start:end])
#         print("-------------")
#         i += len(board)
#     print("=====================")
