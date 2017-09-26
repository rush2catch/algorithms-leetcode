# Problem: Happy Number
# Difficulty: Easy
# Category: Math
# Leetcode 202: https://leetcode.com/problems/happy-number/description/
"""
Write an algorithm to determine if a number is "happy".
A happy number is a number defined by the following process:
Starting with any positive integer, replace the number by the sum of the squares of its digits,
and repeat the process until the number equals 1 (where it will stay),
or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy numbers.
Example: 19 is a happy number
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
"""


class Solution(object):
	def happy_number(self, n):
		if n <= 0:
			return False
		temp = set()
		while n != 1:
			n = sum([int(i) ** 2 for i in str(n)])
			if n in temp:
				return False
			else:
				temp.add(n)
		else:
			return True

obj = Solution()
print(obj.happy_number(37))
print(obj.happy_number(19))