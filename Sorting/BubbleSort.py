# Bubble Sort


class Solution(object):
    def bubble_sort(self, nums):
        for i in range(len(nums)):
            for j in range(len(nums) - 1):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
        return nums


obj = Solution()
print(obj.bubble_sort([6,53,32,76,223,771,0,1]))