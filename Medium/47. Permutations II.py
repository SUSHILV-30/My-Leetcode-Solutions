class Solution(object):
    def permuteUnique(self, nums):
        result = []
        def backtrack(current,remaining):
            if not remaining:
                result.append(current[:])
                return
            used = []
            for i in range(len(remaining)):
                if remaining[i] in used:
                    continue
                used.append(remaining[i])
                current.append(remaining[i])
                backtrack(current,remaining[:i]+remaining[i+1:])
                current.pop()


        

        backtrack([],nums)
        return result

        
