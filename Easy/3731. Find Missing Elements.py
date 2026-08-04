class Solution:
    def findMissingElements(self, nums):
        s = set(nums)
        lo, hi = min(nums), max(nums)
        return [x for x in range(lo, hi + 1) if x not in s]
