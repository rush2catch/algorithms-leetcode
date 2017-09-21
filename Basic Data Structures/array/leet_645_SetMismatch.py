# Problem: Set Mismatch
# Difficulty: Easy
# Category: Array
# Leetcode 645: https://leetcode.com/problems/set-mismatch/description/
# Description:
"""
The set S originally contains numbers from 1 to n.
But unfortunately, due to the data error,
one of the numbers in the set got duplicated to another number in the set,
which results in repetition of one number and loss of another number.
Given an array nums representing the data status of this set after the error.
Your task is to firstly find the number occurs twice and then find the number that is missing.
Return them in the form of an array.

Example 1:
Input: nums = [1,2,2,4]
Output: [2,3]
"""


class Solution(object):
	def find_mismatch(self, nums):
		n = len(nums)
		i = 0
		duplicate  =0
		missing = 0
		while i < n:
			if nums[i] != i + 1 and nums[i] != nums[nums[i] - 1]:
				temp = nums[nums[i] - 1]
				nums[nums[i] - 1] = nums[i]
				nums[i] = temp
			else:
				i += 1

		for i in range(len(nums)):
			if nums[i] != i + 1:
				duplicate = nums[i]
				missing = i + 1

		return [duplicate, missing]

obj = Solution()
arr1 = [1, 2, 2, 4]
arr2 = [1, 2, 3, 2]
arr3 = [1, 2, 2, 3]
print(obj.find_mismatch(arr1))
print(obj.find_mismatch(arr2))
print(obj.find_mismatch(arr3))