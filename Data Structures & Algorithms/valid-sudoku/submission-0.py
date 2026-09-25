class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            hashmap = set()
            for j in range(9):
                if board[i][j] != '.':
                    if board[i][j] in hashmap:
                        return False
                    hashmap.add(board[i][j])

        for j in range(9):
            hashmap = set()
            for i in range(9):
                if board[i][j] != '.':
                    if board[i][j] in hashmap:
                        return False
                    hashmap.add(board[i][j])

        for square in range(9):
            hashmap = set()
            for i in range(3):
                for j in range(3):
                    row = (square//3) * 3 + i
                    col = (square % 3) * 3 + j
                    if board[row][col] != '.':
                        if board[row][col] in hashmap:
                            return False
                        hashmap.add(board[row][col])
        return True