class Solution(object):
    def isValidSudoku(self, board):

        if len(board) != 9:
            return False

        # ROWS
        for i in range(9):

            if len(board[i]) != 9:
                return False

            used = []

            for j in range(9):

                if board[i][j] == ".":
                    continue

                if board[i][j] in used:
                    return False

                used.append(board[i][j])

        # COLUMNS
        for j in range(9):

            used = []

            for i in range(9):

                if board[i][j] == ".":
                    continue

                if board[i][j] in used:
                    return False

                used.append(board[i][j])

        # 3 x 3 BOXES
        for row in range(0, 9, 3):

            for col in range(0, 9, 3):

                used = []

                for i in range(row, row + 3):

                    for j in range(col, col + 3):

                        if board[i][j] == ".":
                            continue

                        if board[i][j] in used:
                            return False

                        used.append(board[i][j])

        return True
