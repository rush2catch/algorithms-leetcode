# Problem: Two Sum II - input array is sorted
# Difficulty: Easy
# Category: Array/Hash Table
# Leetcode 167: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/#/description
# Description:
"""
Given an array of integers that is already sorted in ascending order,
find two numbers such that they add up to a specific target number.
The function twoSum should return indices of the two numbers such that they add up to the target,
where index1 must be less than index2.
Please note that your returned answers (both index1 and index2) are not zero-based.
You may assume that each input would have exactly one solution and you may not use the same element twice.

Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2
"""


class Solution(object):

	def two_sum_1(self, nums, target):
	# a two pointer method
		if len(nums) == 0:
			return -1
		low = 0
		high = len(nums) - 1
		res = ()
		while low < high:
			ans = nums[low] + nums[high]
			if ans < target:
				low += 1
			if ans > target:
				high -= 1
			if ans == target:
				return (low+1, high+1)
		raise ValueError("No Solution")

	def two_sum_2(self, nums, target):
	# a binary search solution
		if len(nums) == 0:
			return None

		for i in range(len(nums)):
			ans = target  - nums[i]
			pos = self.binary_search(ans, nums[i+1:])
			if pos != -1:
				return (i+1, i+pos+1)
		return None

	def binary_search(self, target, nums):
		if len(nums) == 0:
			return -1
		low = 0
		high = len(nums) - 1

		while low <= high:
			mid = (low + high) // 2
			if nums[mid] < target:
				low = mid + 1
			if nums[mid] > target:
				high = mid - 1
			if nums[mid] == target:
				return mid + 1
		raise  ValueError("No Solution")

obj = Solution()
testNums1 = [2, 7, 11, 15]
print(obj.two_sum_1(testNums1, 9))
print(obj.two_sum_2(testNums1, 9))
