class Solution(object):
    def gcdOfOddEvenSums(self, n):
        sum1,sum2 = 0,0
        for i in range(1,2*n+1):
            if i%2 != 0:
                sum1 = sum1+i
            else:
                sum2=sum2+i
        while sum2!=0:
            sum1,sum2 = sum2,sum1%sum2
        return sum1


        
