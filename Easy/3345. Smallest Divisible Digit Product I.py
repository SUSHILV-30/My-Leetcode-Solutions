class Solution(object):
    def smallestNumber(self,n, t):
        def digit_product(x):
            p = 1
            for c in str(x):
                p *= int(c)
            return p

        while digit_product(n) % t != 0:
            n += 1
        return n
        
        
