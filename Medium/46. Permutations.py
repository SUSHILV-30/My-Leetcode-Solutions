class Solution(object):
    def permute(self, nums):
        result = []
        def backtrack(current,remaining):
            if not remaining:
                result.append(current[:])

            for i in range(len(remaining)):
                current.append(remaining[i])
                backtrack(current,remaining[:i] + remaining[i+1:])
                current.pop()
        
        backtrack([],nums)
        return result
