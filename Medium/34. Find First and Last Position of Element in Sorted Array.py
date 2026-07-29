class Solution(object):
    def searchRange(self, nums, target):
        def leftmost():
            low,high = 0,len(nums)-1

            while low<= high:
                mid = (low+high)//2

                if nums[mid]<target:
                    low = mid+1
                else:
                    high = mid-1
            return low
        def rightmost():
            low,high = 0,len(nums)-1

            while low<= high:
                mid = (low+high)//2

                if nums[mid]<=target:
                    low = mid+1
                else:
                    high = mid-1
            return high
        left = leftmost()
        right = rightmost()

        if left == len(nums) or nums[left]!= target:
            return [-1,-1]

        return [left,right]
