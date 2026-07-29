class Solution(object):
    def searchMatrix(self, matrix, target):
        if not matrix or not matrix[0]:
            return False
        m, n = len(matrix), len(matrix[0])
        low,high = 0,m*n-1

        while low<=high:
            mid = (low+high)//2

            row = mid//n
            col = mid%n
            val = matrix[row][col]

            if val == target:
                return True
            elif val < target:
                low = mid+1

            else:
                high = mid-1
        return False

        
