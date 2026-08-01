class Solution(object):
    def longestPalindrome(self, s):
        if not s:
            return ""

        start, end = 0, 0

        def expand(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return right - left - 1  # length of palindrome found

        for i in range(len(s)):
            len1 = expand(i, i)       # odd length, center at i
            len2 = expand(i, i + 1)   # even length, center between i, i+1
            curr_max = max(len1, len2)

            if curr_max > end - start + 1:
                start = i - (curr_max - 1) // 2
                end = i + curr_max // 2

        return s[start:end + 1]
