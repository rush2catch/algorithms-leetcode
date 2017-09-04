# Problem: Divide Two Integers
# Difficulty: Medium
# Category: Math
# Leetcode 29: https://leetcode.com/problems/divide-two-integers/description/
# Description:
"""
Divide two integers without using multiplication, division and mod operator.
If it is overflow, return MAX_INT.
"""


class Solution(object):

	def divide_integer(self, dividend, divider):
		if dividend > 0 and divider == 0:
			return 2147483647
		if dividend < 0 and divider == 0:
			return - 2147483647
		sign = (divider >= 0) is (dividend >= 0)
		dividend = abs(dividend)
		divider = abs(divider)
		res = 0

		while dividend >= divider:
			temp = divider
			i = 1
			while dividend >= temp:
				dividend -= temp
				res += i
				i <<= 1
				temp <<= 1

		if not sign:
			res = -res
		return min(max(-2147483648, res), 2147483647)

obj = Solution()
print(obj.divide_integer(10, 2))
print(obj.divide_integer(-1, 0))
print(obj.divide_integer(15, -5))
print(obj.divide_integer(-1 , -1))

