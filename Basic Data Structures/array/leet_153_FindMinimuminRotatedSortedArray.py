# Problem: Find Minimum in Rotated Sorted Array
# Difficulty: Medium
# Category: Array
# Leetcode 153: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/
"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
Find the minimum element.
You may assume no duplicate exists in the array.
"""


class Solution(object):
	def find_mini(self, nums):
		if len(nums) == 0:
			return None
		start = 0
		end = len(nums) - 1
		while start < end:
			mid = (start + end) // 2
			if nums[mid] < nums[end]:
				end = mid
			else:
				start = mid + 1
		return nums[start]


obj = Solution()
arr1 = [4, 5, 6, 7, 0, 1, 2]
arr2 = [0, 1, 2]
arr3 = [1]
print(obj.find_mini(arr1), obj.find_mini(arr2), obj.find_mini(arr3))