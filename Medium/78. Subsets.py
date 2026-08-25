class Solution(object):
    def subsets(self, nums):
        result = []
        def backtrack(index,choices,result):
            
            result.append(choices[:])

            
            for i in range(index,len(nums)):
                
                choices.append(nums[i])
                backtrack(i+1,choices,result)
                choices.pop()
        backtrack(0,[],result)
        return result


        
