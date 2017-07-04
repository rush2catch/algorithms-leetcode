# Problem:  Third Maximum Number
# Difficulty: Easy
# Category: Array
# Leetcode 414: https://leetcode.com/problems/third-maximum-number/#/description
# Description:
"""
Given a non-empty array of integers, return the third maximum number in this array.
If it does not exist, return the maximum number. The time complexity must be in O(n).

Example 1:
Input: [3, 2, 1]
Output: 1
Explanation: The third maximum is 1.

Example 2:
Input: [1, 2]
Output: 2
Explanation: The third maximum does not exist, so the maximum (2) is returned instead.

Example 3:
Input: [2, 2, 3, 1]
Output: 1
Explanation: Note that the third maximum here means the third maximum distinct number.
Both numbers with value 2 are both considered as second maximum.
"""


class Solution(object):
	def third_max_number(self, nums):

		# initialize
		maximum, middle, minimum = 0, 0, 0

		# corner case
		if len(nums) == 1:
			return nums[0]

		if len(nums) == 2:
			return max(nums[0], nums[1])

		for i in range(len(nums)):
			if nums[i] not in (minimum, middle, maximum):
				if nums[i] > maximum:
					minimum = middle
					middle = maximum
					maximum = nums[i]
				elif middle < nums[i] < maximum:
					minimum = middle
					middle = nums[i]
				elif minimum < nums[i] < middle:
					minimum = nums[i]
				else:
					pass

		if minimum == 0:
			return maximum
		else:
			return minimum


obj = Solution()
test_case1 = [3, 2, 1]
test_case2 = [2, 1]
test_case3 = [2, 2, 3, 1]
test_case4 = [1, 5, 5, 5]
test_case5 = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]
print(obj.third_max_number(test_case1))
print(obj.third_max_number(test_case2))
print(obj.third_max_number(test_case3))
print(obj.third_max_number(test_case4))
print(obj.third_max_number(test_case5))

