class Solution(object):
    def merge(self, nums1, m, nums2, n):
        n1 = len(nums1)
        n2 = len(nums2)

        real1 = nums1[:m]      # keep only the actual m elements, drop the padding zeros
        real2 = nums2[:n]      # keep only the actual n elements

        nums3 = sorted(real1 + real2)

        nums1[:] = nums3       # <-- this is the missing piece: write back into nums1 in place
        return nums1
        
        
