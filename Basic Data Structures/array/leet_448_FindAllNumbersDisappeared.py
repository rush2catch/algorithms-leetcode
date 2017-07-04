# Problem: Find All Numbers Disappeared in an Array
# Difficulty: Easy
# Category: Array
# Leetcode 448: https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/#/description
# Description:
"""
Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.
Find all the elements of [1, n] inclusive that do not appear in this array.
Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

Example:
Input:
[4,3,2,7,8,2,3,1]
Output:
[5,6]
"""


class Solution(object):

	# solution with extra O(n) space and with O(n) time complexity(append() takes O(1) time)
	def find_disappeared_numbers(self, nums):
		full_array = []
		for i in range(1, len(nums)):
			full_array.append(i)
		return list(set(full_array).difference(set(nums)))

	# solution without extra space but with O(n^2) time complexity (x in s takes O(n) time)
	def find_missing_numbers(self, nums):
		result = []
		for i in range(len(nums)):
			if i+1 not in nums:
				result.append(i+1)
		return result

obj = Solution()
test_case1 = [4, 3, 2, 7, 8, 2, 3, 1]
print(obj.find_disappeared_numbers(test_case1))
print(obj.find_missing_numbers(test_case1))