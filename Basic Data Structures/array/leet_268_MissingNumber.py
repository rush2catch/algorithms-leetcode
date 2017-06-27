# Problem: Missing Number
# Difficulty: Easy
# Category: Array
# Leetcode 268:https://leetcode.com/problems/missing-number/#/description
# Description:
"""
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n,
find the one that is missing from the array.

For example,
Given nums = [0, 1, 3] return 2.

Note:
Your algorithm should run in linear runtime complexity.
Could you implement it using only constant extra space complexity?
"""

class Solution(object):
	def missingNumber(self, nums):
		"""
		:param nums: list[int]
		:return: int
		"""
		if len(nums) == 0:
			return None
		if len(nums) == 1 and nums[0] == 1:
			return 0
		i = 0
		while i < len(nums):
			if nums[i] == i:
				i += 1
			if nums[i] == i + 1:
				return i

obj = Solution()
test_nums = [0, 1, 3]
print(obj.missingNumber(test_nums))