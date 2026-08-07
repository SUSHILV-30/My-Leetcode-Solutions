class Solution(object):
    def sumAndMultiply(self, n):
        s = str(n)
        sum = 0
        res1 = 0
        list1 = []
        for i in s:
            list1.append(i)
        
        list1 = [i for i in list1 if i != "0"] 

        for j in list1:
            res = int(j)
            sum = sum+res
            res1 = res1*10+res
    
        res2 = res1*sum
        return res2
