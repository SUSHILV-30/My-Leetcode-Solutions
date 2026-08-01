class Solution(object):
    def climbStairs(self, n):
        memo = {}

        def climb(current):
            if current == n:
                return 1
            if current > n:
                return 0
            if current in memo:
                return memo[current]

            memo[current] = climb(current + 1) + climb(current + 2)
            return memo[current]

        return climb(0)
