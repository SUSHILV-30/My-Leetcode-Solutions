class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        nums3 = sorted(nums1 + nums2)
        n1 = len(nums3)

        if n1 % 2 == 0:
            ind = n1 // 2
            res = (nums3[ind - 1] + nums3[ind]) / 2.0
        else:
            ind = n1 // 2
            res = float(nums3[ind])

        return res
