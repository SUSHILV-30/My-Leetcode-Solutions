class Solution(object):
    def isPalindrome(self, x):
        original = x
        x=abs(x)
        reversednum=0
        x2=0
        

        while x != 0:
            x2=x%10
            reversednum=reversednum*10+x2
            x //= 10
    
        result = False if original<0 or (original != reversednum) else True

        return result

       
