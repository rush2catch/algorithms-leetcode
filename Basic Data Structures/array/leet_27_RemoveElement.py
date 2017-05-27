# Problem: Remove Element
# Difficulty: Easy
# Category: Array/Two Pointers
# Leetcode 27: https://leetcode.com/problems/remove-element/#/description
# Description:
"""
Given an array and a value, remove all instances of that value in place and return the new length.
Do not allocate extra space for another array, you must do this in place with constant memory.
The order of elements can be changed. It doesn't matter what you leave beyond the new length.
Example:Given input array nums = [3,2,2,3], val = 3
Your function should return length = 2, with the first two elements of nums being 2.
"""


class Solution(object):
    def remove_element(self, nums, val):
        if len(nums) <= 0:
            return -1

        i = 0
        while i < len(nums):
            if nums[i] == val:
                nums.pop(i)
            else:
                i += 1
        return len(nums)

obj = Solution()
print(obj.remove_element([2, 3, 3, 2], 3))