class Solution(object):
    def maxProduct(self, nums):
        n = len(nums)
        result = 0
        for i in range(n):
            for j in range(n):
                if i !=j:
                    total = ((nums[i]-1) * (nums[j]-1))
                    if total >= result:
                        result = total

        return result


        
