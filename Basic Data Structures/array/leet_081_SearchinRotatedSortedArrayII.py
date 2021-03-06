# Problem: Search in Rotated Sorted Array II
# Difficulty: Medium
# Category: Array
# Leetcode 81: https://leetcode.com/problems/search-in-rotated-sorted-array-ii/description/
"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
You are given a target value to search. If found in the array return its index, otherwise return -1.
You may assume no duplicate exists in the array.
"""


class Solution(object):

	def search(self, nums, target):
		if len(nums) == 0:
			return False
		left = 0
		right = len(nums) - 1

		while left <= right:
			mid = (left + right) // 2
			if nums[mid] == target:
				return True
			elif nums[mid] > nums[left] or nums[mid] > nums[right]:
				if target < nums[mid] and target >= nums[left]:
					right = mid - 1
				else:
					left = mid + 1
			elif nums[mid] < nums[right] or nums[mid] < nums[left]:
				if target <= nums[right] and target > nums[mid]:
					left = mid + 1
				else:
					right = mid - 1
			else:
				right -= 1
		return False


obj = Solution()
arr1 = [4, 5, 6, 7, 0, 0, 0, 0, 1, 2]
print(obj.search(arr1, 0))
