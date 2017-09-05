# Problem: Sum of Squares
# Difficulty: Easy
# Category: Math
# Leetcode 633: https://leetcode.com/problems/sum-of-square-numbers/description/
# Description:
"""
Given a non-negative integer c, your task is to decide whether there're two integers a and b such that a2 + b2 = c.

Example 1:
Input: 5
Output: True
Explanation: 1 * 1 + 2 * 2 = 5
Example 2:
Input: 3
Output: False
"""


class Solution(object):
	def judgeSquareSum(self, c):

		if c == 0 or c == 1:
			return True
		a = 0
		while a * a <= c:
			b = c - a * a
			if self.isSqrt(b):
				return True
			a += 1
		return False

	def isSqrt(self, x):
		if x == 0:
			return True
		left = 0
		right = x

		while left <= right:
			mid = left + (right - left) // 2
			if mid * mid <= x < (mid + 1) * (mid + 1):
				ans = mid
				break
			elif mid * mid > x:
				right = mid
			else:
				left = mid + 1

		if ans * ans == x:
			return True
		else:
			return False

obj = Solution()
print(obj.judgeSquareSum(2147483643))