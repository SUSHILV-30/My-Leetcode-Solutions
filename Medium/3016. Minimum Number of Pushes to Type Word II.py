class Solution(object):
    def minimumPushes(self, word):
        from collections import Counter

class Solution:
    def minimumPushes(self, word):
        freq = sorted(Counter(word).values(), reverse=True)
        total = 0
        for i, f in enumerate(freq):
            cost = (i // 8) + 1
            total += cost * f
        return total
        
