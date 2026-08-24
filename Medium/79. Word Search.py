class Solution(object):
    def exist(self, board, word):

        def backtrack(r, c, index):

            
            if index == len(word):
                return True

            
            if (r < 0 or r >= len(board) or
                c < 0 or c >= len(board[0]) or
                board[r][c] != word[index]):
                return False

            
            temp = board[r][c]
            board[r][c] = '#'

            
            found = (
                backtrack(r + 1, c, index + 1) or
                backtrack(r - 1, c, index + 1) or
                backtrack(r, c + 1, index + 1) or
                backtrack(r, c - 1, index + 1)
            )

            
            board[r][c] = temp

            return found

        
        for r in range(len(board)):
            for c in range(len(board[0])):

                if backtrack(r, c, 0):
                    return True

        return False
