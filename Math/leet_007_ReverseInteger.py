# Problem:  Reverser Integer
# Difficulty: Easy
# Category: Math
# Leetcode 007: https://leetcode.com/problems/reverse-integer/description/
"""
Reverse digits of an integer.
Example1: x = 123, return 321
Example2: x = -123, return -321

Here are some good questions to ask before coding. Bonus points for you if you have already thought through this!
If the integer's last digit is 0, what should the output be? ie, cases such as 10, 100.
Did you notice that the reversed integer might overflow? Assume the input is a 32-bit integer,
then the reverse of 1000000003 overflows. How should you handle such cases?
For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
"""


class Solution(object):

	def reverse_integer(self, n):
		ans = 0
		sign = -1 if n < 0 else 1
		num = abs(n)
		while num != 0:
			tail = num % 10
			ans = ans * 10 + tail
			num = num // 10

		if ans > 0x7FFFFFFF:
			return 0
		else:
			return ans * sign

obj = Solution()
print(obj.reverse_integer(-123))
print(obj.reverse_integer(-99999999999991134455524555324555333555))
print(obj.reverse_integer(0))
print(obj.reverse_integer(100100))