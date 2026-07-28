class Solution(object):
    def firstMissingPositive(self, nums):
        n = len(nums)
        
        # Step 1: place each number v (1<=v<=n) at index v-1
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                correct_idx = nums[i] - 1
                nums[i], nums[correct_idx] = nums[correct_idx], nums[i]
        
        # Step 2: find first index where value doesn't match index+1
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        
        # all positions 1..n are filled correctly
        return n + 1
