class Solution():
    def lengthOfLongestSubstring(self,s):
        seen={}
        left=0
        max1=0

        for right,char in enumerate(s):

            if char in seen and seen[char]>=left:
                left = seen[char]+1

            seen[char]=right
            max1 = max(max1,right-left + 1)

        return max1
