class Solution(object):
    def divide(self, dividend, divisor):
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1

        if dividend == INT_MIN and divisor == -1:
            return INT_MAX

        negative = (dividend < 0) != (divisor < 0)
        
        a = abs(dividend)
        b = abs(divisor)
        result = 0

        while a >= b:        # fix: replace for loop with while
            temp = b
            multiple = 1
            while a >= (temp << 1):
                temp <<= 1
                multiple <<= 1
            a -= temp
            result += multiple

        if negative:
            return max(-result, INT_MIN)
        return min(result, INT_MAX)
