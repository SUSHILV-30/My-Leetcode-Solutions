class Solution(object):
    def fourSum(self, nums, target):
        nums.sort()
        n = len(nums)
        seen = set()
        list1 = []
        for i in range(n - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            for j in range(i + 1, n - 2):          # fixed: start at i+1
                if j > i + 1 and nums[j] == nums[j - 1]:   # fixed: baseline i+1
                    continue

                left, right = j + 1, n - 1

                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]
                    if total == target:
                        list1.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1
                        right -= 1
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while left < right and nums[right] == nums[right + 1]:  # fixed
                            right -= 1
                    elif total < target:
                        left += 1
                    else:
                        right -= 1

        return list1
