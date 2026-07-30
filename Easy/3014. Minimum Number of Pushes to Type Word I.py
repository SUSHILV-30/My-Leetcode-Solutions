class Solution(object):
    def minimumPushes(self, word):
        n = len(word)
        keys =8

        count =0
        total = 0
        pushes = 1

        for i in range(n):
            if count == keys:
                count = 0
                pushes+=1

            total+=pushes
            count+=1

        return total
        
