class Solution(object):
    def solveSudoku(self, board):

        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        # Store existing numbers
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    num = board[i][j]
                    box = (i // 3) * 3 + (j // 3)

                    rows[i].add(num)
                    cols[j].add(num)
                    boxes[box].add(num)

        def backtrack():

            # Find the empty cell with minimum choices
            min_options = 10
            best_row = -1
            best_col = -1
            best_box = -1

            for i in range(9):
                for j in range(9):

                    if board[i][j] == ".":

                        box = (i // 3) * 3 + (j // 3)

                        options = 0

                        for num in "123456789":
                            if (num not in rows[i] and
                                num not in cols[j] and
                                num not in boxes[box]):
                                options += 1

                        if options < min_options:
                            min_options = options
                            best_row = i
                            best_col = j
                            best_box = box

            # No empty cells → Sudoku solved
            if best_row == -1:
                return True

            # No possible number → wrong path
            if min_options == 0:
                return False

            # Try numbers
            for num in "123456789":

                if (num not in rows[best_row] and
                    num not in cols[best_col] and
                    num not in boxes[best_box]):

                    # MAKE
                    board[best_row][best_col] = num
                    rows[best_row].add(num)
                    cols[best_col].add(num)
                    boxes[best_box].add(num)

                    # EXPLORE
                    if backtrack():
                        return True

                    # UNDO
                    board[best_row][best_col] = "."
                    rows[best_row].remove(num)
                    cols[best_col].remove(num)
                    boxes[best_box].remove(num)

            return False

        backtrack()
