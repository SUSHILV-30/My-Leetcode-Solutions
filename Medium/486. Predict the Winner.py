class Solution(object):
    def PredictTheWinner(self, nums):
        memo = {}

        def best_diff(left, right):
            if left == right:
                return nums[left]

            if (left, right) in memo:
                return memo[(left, right)]

            # Choosing left end: gain nums[left], then opponent plays optimally
            # on nums[left+1..right], so subtract their best difference.
            pick_left = nums[left] - best_diff(left + 1, right)

            # Choosing right end: same idea, mirrored.
            pick_right = nums[right] - best_diff(left, right - 1)

            memo[(left, right)] = max(pick_left, pick_right)
            return memo[(left, right)]

        return best_diff(0, len(nums) - 1) >= 0
