# Problem: Sqrt(x)
# Difficulty: Easy
# Category: Math
# Leetcode 69: https://leetcode.com/problems/sqrtx/discuss/
# Description:
"""
Implement int sqrt(int x).

Compute and return the square root of x.
"""


class Solution(object):
	def sqrt(self, x):
		if x == 0:
			return 0
		if x < 0:
			raise ValueError('x should not be negative')
		left = 1
		right = x

		while left <= right:
			mid = left + (right - left) // 2
			if mid * mid <= x < (mid + 1) * (mid + 1):
				if (x - mid * mid) > ((mid + 1)*(mid + 1) - x):
					return mid + 1
				else:
					return mid
			elif mid * mid > x:
				right = mid
			else:
				left = mid + 1

obj = Solution()
print(obj.sqrt(100))
print(obj.sqrt(121))
print(obj.sqrt(63))
print(obj.sqrt(65))

