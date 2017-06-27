# Problem: Search Insert Position
# Difficulty: Easy
# Category: Array
# Leetcode 35:https://leetcode.com/problems/search-insert-position/#/description
# Description:
"""
Given a sorted array and a target value, return the index if the target is found.
If not, return the index where it would be if it were inserted in order.
You may assume no duplicates in the array.
Here are few examples.
[1,3,5,6], 5 → 2
[1,3,5,6], 2 → 1
[1,3,5,6], 7 → 4
[1,3,5,6], 0 → 0
"""

class Solution(object):
	def searchInsert(self, nums, target):
		"""
	    :param nums: List[int]
	    :param target: int
	    :return: int
	    """
		if len(nums) == 0:
			return None
		if target < nums[0]:
			return 0
		if target > nums[len(nums) - 1]:
			return len(nums)

		for i in range(len(nums)):
			if nums[i] == target:
				return i
			elif nums[i] < target and target < nums[i + 1]:
				return i+1

test_list = [1, 3, 5, 6]
obj = Solution()
print(obj.searchInsert(test_list, 5))
print(obj.searchInsert(test_list, 2))
print(obj.searchInsert(test_list, 7))
print(obj.searchInsert(test_list, 0))