class Solution(object):
    def maxArea(self, height):
        maxarea = 0
        i = 0
        j = len(height) - 1

        for _ in height:
            if i >= j:
                break
            area = min(height[i], height[j]) * (j - i)
            if area > maxarea:
                maxarea = area
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1

        return maxarea
