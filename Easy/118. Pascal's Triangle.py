class Solution(object):
    def generate(self, numRows):
        
        list2 = []
        for i in range(numRows):
            list1 = []
            for j in range(i+1):
                if j == 0 or j==i:
                    list1.append(1)
                    
                else:
                    prev = list2[i-1]
                    res = prev[j-1] + prev[j]
                    list1.append(res)

            list2.append(list1)

        return list2
                    
        
