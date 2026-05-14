class Solution(object):
    def searchInsert(self, nums, target):
        count = 0
        for i,x in enumerate(nums):
            if x == target:
                return i
                count=count+1

        if count == 0:
            for i,x in enumerate(nums):
                if i== 0 and target<nums[i]:
                    nums[0] = target
                    return i

                elif target<nums[i] and target>nums[i-1]:
                    nums[i] = target
                    return i
                
                elif target>nums[len(nums)-1]:
                    nums.append(target)
                    i = len(nums)-1
                    return i

            
        
