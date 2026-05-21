class Solution(object):
    def removeElement(self, nums, val):
        count=0
        list_1=[]
        for i,x in enumerate(nums):
            if x != val:
                nums[count] = x
                count=count+1
                

        return count 


        
