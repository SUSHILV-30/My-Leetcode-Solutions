class Solution(object):
    def myPow(self, x, n):
        if n < 0:
            x = 1 / x
            n = -n

        res = 1
        while n > 0:
            if n % 2 == 1:      # n is odd, peel off one factor of x
                res *= x
            x *= x               # square x
            n //= 2               # halve n
        return res
