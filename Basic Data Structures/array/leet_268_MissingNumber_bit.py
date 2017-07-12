# Problem: Missing Number
# Difficulty: Easy
# Category: Array
# Leetcode 268:https://leetcode.com/problems/missing-number/#/description
# Description:
"""
Given an sorted array containing n distinct numbers taken from 0, 1, 2, ..., n,
find the one that is missing from the array.

For example,
Given nums = [0, 1, 3] return 2.

Note:
Your algorithm should run in linear runtime complexity.
Could you implement it using only constant extra space complexity?
"""


class Solution(object):

	def bit_manipulation(self, nums):
		missing = 0
		i = 0
		while i < len(nums):
			missing = missing ^ i ^ nums[i]
			i += 1
		return missing ^ i


obj = Solution()
nums1 = [7, 5, 3, 4, 1, 0, 2]
nums2 = [3, 0, 1, 2]
print(obj.bit_manipulation(nums1))
print(obj.bit_manipulation(nums2))