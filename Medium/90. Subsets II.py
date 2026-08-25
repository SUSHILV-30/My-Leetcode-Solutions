class Solution(object):
    def subsetsWithDup(self, nums):
        result = []
        nums.sort()
        def backtrack(index,choices,result):
            result.append(choices[:])
            for i in range(index,len(nums)):
                if (i>index and nums[i] == nums[i-1]):
                    continue
                choices.append(nums[i])
                backtrack(i+1,choices,result)
                choices.pop()

        backtrack(0,[],result)
        return result        
