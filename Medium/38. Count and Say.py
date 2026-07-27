class Solution(object):
    def countAndSay(self, n):
        if n ==1:
            return "1"
        
        else:
            return self.rle(self.countAndSay(n-1))

    def rle(self,s):
        encoded = []
        i = 0
        n = len(s)

        while i<n:
            char = s[i]
            count = 1

            while i+1 < n and s[i+1] == char:
                i+=1
                count+=1

            encoded.append(str(count))
            encoded.append(char)
            i+=1
        return ''.join(encoded)
            
        
