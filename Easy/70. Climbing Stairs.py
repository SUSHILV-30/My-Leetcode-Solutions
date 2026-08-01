class Solution(object):
    def climbStairs(self, n):
        count =[0]

        def climb(current):
            
            if current == n:
                count[0]+=1
                return
            elif current>n:
                return

            climb(current+1)
            climb(current+2)

        climb(0)
        return count[0]
