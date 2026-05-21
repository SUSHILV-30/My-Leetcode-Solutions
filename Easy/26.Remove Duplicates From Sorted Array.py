class Solution(object):
    def removeDuplicates(self, nums):
        k=1
        i=0
        if len(nums) == 0:
            return 0
        for i in range(i,len(nums)):
            if nums[i] != nums[k-1]:
                nums[k]=nums[i]
                k=k+1
        
        return k
    
