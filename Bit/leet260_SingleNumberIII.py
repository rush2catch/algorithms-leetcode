# Problem: Single Number III
# Difficulty: Medium
# Category: Bit Manipulation
# Leetcode 260: https://leetcode.com/problems/single-number-iii/description/
# Description:
"""
Given an array of numbers nums,
in which exactly two elements appear only once and all the other elements appear exactly twice.
Find the two elements that appear only once.
For example:
Given nums = [1, 2, 1, 3, 2, 5], return [3, 5].
Note:
The order of the result is not important. So in the above example, [5, 3] is also correct.
Your algorithm should run in linear runtime complexity. Could you implement it using only constant space complexity?
"""


class Solution(object):
	def single_number(self, nums):
		xor = 0
		a = 0
		b = 0
		for num in nums:
			xor ^= num
		mask = 1
		while mask & xor == 0:
			mask = mask << 1
		for num in nums:
			if mask & num:
				a ^= num
			else:
				b ^= num
		return [a, b]

obj = Solution()
a1 = [1, 2, 1, 3, 2, 5]
print(obj.single_number(a1))