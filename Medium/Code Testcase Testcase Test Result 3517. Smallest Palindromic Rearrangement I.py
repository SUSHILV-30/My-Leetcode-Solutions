from collections import Counter
class Solution(object):
    def smallestPalindrome(self, s):
        cnt = Counter(s)
        left1 = []
        mid =''

        for ch in sorted(cnt):
            half = cnt[ch]//2

            if half:
                left1.append(ch*half)

            if cnt[ch]%2:
                mid = ch

        left = ''.join(left1)
        return left+mid+left[::-1]        

        
