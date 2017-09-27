# Problem: Missing Number
# Difficulty: Easy
# Category: Array
# Leetcode 268:https://leetcode.com/problems/missing-number/#/description
# Description:
"""
Given an sorted containing n distinct numbers taken from 0, 1, 2, ..., n,
find the one that is missing from the array.

For example,
Given nums = [0, 1, 3] return 2.

Note:
Your algorithm should run in linear runtime complexity.
Could you implement it using only constant extra space complexity?
"""

# please note that the given array is not necessarily sorted, the example above is really confusing.


class Solution(object):

	# solution 2: less code
	def missing_number_2(self, nums):
		"""
		:param nums: List[int]
		:return: int
		"""
		n = len(nums)
		traceZero = True
		max = 0
		for i in range(len(nums)):
			if nums[i] == 0:
				traceZero = False
			if nums[i] >= max:
				max = nums[i]

		if traceZero:
			return 0
		if not traceZero:
			if max == len(nums):
				return int(n * (n + 1) / 2) - sum(nums)
			if max == len(nums) - 1:
				return None


obj = Solution()
test_case1 = [0, 1, 5, 4, 3]
test_case2 = [0, 1, 5, 3, 4, 2]
test_case3 = [2, 4, 3, 1, 0]
test_case4 = [3, 6, 4, 2, 1, 5]
test_case5 = [0, 2]
test_case6 = [1, 0]


print(obj.missing_number_2(test_case1))
print(obj.missing_number_2(test_case2))
print(obj.missing_number_2(test_case3))
print(obj.missing_number_2(test_case4))
print(obj.missing_number_2(test_case5))
print(obj.missing_number_2(test_case6))