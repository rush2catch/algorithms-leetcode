# Problem: Longest Continuous Increasing Subsequence
# Difficulty: Easy
# Category: Array
# Leetcode 674: https://leetcode.com/problems/longest-continuous-increasing-subsequence/description/
"""
Given an unsorted array of integers, find the length of longest continuous increasing subsequence.
"""


class Solution(object):

	def find_length(self, nums):
		if len(nums) == 0:
			return 0
		start = 0
		end = 1
		maxLength = 1
		while end < len(nums):
			if nums[end] > nums[end - 1]:
				maxLength = max(maxLength, end - start + 1 )
			else:
				start = end
			end += 1
		return maxLength

obj = Solution()
print(obj.find_length([1, 2, 3, 5, 4, 7]))
print(obj.find_length([1, 2, 3, 3, 2, 1, 4]))
print(obj.find_length([1, 1, 1, 1, 1]))
print(obj.find_length([1, 3, 5, 7]))
print(obj.find_length([1, 3, 5, 4, 2, 3, 4, 5]))