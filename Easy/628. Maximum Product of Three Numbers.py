class Solution(object):
    def maximumProduct(self, nums):
        nums.sort()
        n = len(nums)
        # Case 1: three largest numbers
        candidate1 = nums[-1] * nums[-2] * nums[-3]
        # Case 2: two smallest (possibly negative) * largest
        candidate2 = nums[0] * nums[1] * nums[-1]
        return max(candidate1, candidate2)
        
