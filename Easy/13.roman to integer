class Solution(object):
    def romanToInt(self, s):
        resultnum = 0
        s2 = []

        for i, x in enumerate(s):
            if x == "I":
                s1 = 1
            elif x == "V":
                s1 = 5
            elif x == "X":
                s1 = 10
            elif x == "L":
                s1 = 50
            elif x == "C":
                s1 = 100
            elif x == "D":
                s1 = 500
            elif x == "M":
                s1 = 1000

            s2.append(s1)

            # if current value > previous value → undo previous addition, subtract it instead
            if i != 0 and s2[i] > s2[i-1]:
                resultnum -= 2 * s2[i-1]  # undo +prev, and subtract it → -2*prev

            resultnum += s1

        return resultnum
