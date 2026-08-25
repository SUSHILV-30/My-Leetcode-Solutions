class Solution(object):
    def solveNQueens(self, n):
        result = []
        board=[["."]*n for _ in range(n)]

        def is_valid(row,col):
            for i in range(n):
                if board[i][col] == "Q":
                    return False
                
            i = row-1
            j = col-1
            while i>=0 and j>=0:
                if board[i][j] == "Q":
                    return False
                i-=1
                j-=1
            i = row-1
            j = col+1
            while i>=0 and j<n:
                if board[i][j] == "Q":
                    return False
                i-=1
                j+=1
            return True
        def backtrack(row):
            if row == n:
                solution = []
                for i in range(n):
                    solution.append("".join(board[i]))

                result.append(solution)
                return
            for col in range(n):
                if is_valid(row,col):
                    board[row][col] = "Q"
                    backtrack(row+1)
                    board[row][col] = "."

        backtrack(0)
        return result




        
