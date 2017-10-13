# Problem: Search for a Range
# Difficulty: Medium
# Category: Array
# Leetcode 34: https://leetcode.com/problems/search-for-a-range/description/
"""
Given an array of integers sorted in ascending order, find the starting and ending position of a given target value.
Your algorithm's runtime complexity must be in the order of O(log n).
If the target is not found in the array, return [-1, -1].
For example,
Given [5, 7, 7, 8, 8, 10] and target value 8,
return [3, 4].
"""


class Solution(object):
	def search_range(self, nums, target):
		res = []
		res.append(self.search_left(nums, target))
		res.append(self.search_right(nums, target))
		return res

	def search_left(self, nums, target):
		idx = -1
		lo = 0
		hi = len(nums) - 1
		while lo <= hi:
			mid = (lo + hi) // 2
			if nums[mid] >= target:
				hi = mid - 1
			else:
				lo = mid + 1
			if nums[mid] == target:
				idx = mid
		return idx

	def search_right(self, nums, target):
		idx = -1
		lo = 0
		hi = len(nums) - 1
		while lo <= hi:
			mid = (lo + hi) // 2
			if nums[mid] <= target:
				lo = mid + 1
			else:
				hi = mid - 1
			if nums[mid] == target:
				idx = mid
		return idx


obj = Solution()
a1 = [1, 1, 1, 1, 1]
a2 = [5, 7, 7, 8, 8, 10]
print(obj.search_range(a1, 1))
print(obj.search_range(a2, 8))
