# Problem: Find Pivot Index
# Difficulty: Easy
# Category: Array
# Leetcode 724: https://leetcode.com/problems/find-pivot-index/description/
# Description:
"""
Given an array of integers nums, write a method that returns the "pivot" index of this array.
We define the pivot index as the index where the sum of the numbers
to the left of the index is equal to the sum of the numbers to the right of the index.
If no such index exists, we should return -1.
If there are multiple pivot indexes, you should return the left-most pivot index.

Example 1:
Input:
nums = [1, 7, 3, 6, 5, 6]
Output: 3
Explanation:
The sum of the numbers to the left of index 3 (nums[3] = 6) is equal to the sum of numbers to the right of index 3.
Also, 3 is the first index where this occurs.
Example 2:
Input:
nums = [1, 2, 3]
Output: -1
Explanation:
There is no index that satisfies the conditions in the problem statement.
"""


class Solution(object):

	# A binary search solution
	def find_pivot(self, nums):
		if len(nums) == 0:
			return -1
		pivot = -1
		left = 0
		right = len(nums) - 1
		while left < right:
			mid = (left + right) // 2
			if sum(nums[:mid]) == sum(nums[mid+1:]):
				pivot = mid
				break
			elif sum(nums[:mid]) < sum(nums[mid+1:]):
				left = mid + 1
			else:
				right = mid
		return pivot

	# a O(N) one pass solution
	def pivot_index(self, nums):
		totalSum = sum(nums)
		leftSum = 0
		for i, x in enumerate(nums):
			if leftSum == (totalSum - leftSum - x):
				return i
			leftSum += x
		return -1

obj = Solution()
a1 = [1, 7, 3, 6, 5, 6]
print(obj.find_pivot(a1))
print(obj.pivot_index(a1))