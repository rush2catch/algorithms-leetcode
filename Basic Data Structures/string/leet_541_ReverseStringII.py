# Problem:  Reverse String II
# Difficulty: Easy
# Category: String
# Leetcode 541: https://leetcode.com/problems/reverse-string-ii/#/description
# Description:
"""
Given a string and an integer k,
you need to reverse the first k characters for every 2k characters counting from the start of the string.
If there are less than k characters left, reverse all of them.
If there are less than 2k but greater than or equal to k characters,
then reverse the first k characters and left the other as original.
Example:
Input: s = "abcdefg", k = 2
Output: "bacdfeg"
"""


class Solution(object):

	def reverse_string(self, s, k):
		n = len(s)
		i = 1
		res = ''
		if n == 0 or k == 0 or k == 1:
			return s
		quotient = n // k

		while i <= quotient:
			if i % 2 == 1:
				res += s[(i - 1) * k:i * k][::-1]
			else:
				res += s[(i - 1) * k:i * k]
			i += 1

		if quotient % 2 == 1:
			res += s[quotient * k:n]
		else:
			res += s[quotient * k:n][::-1]
		return res

obj = Solution()
s1 = 'abcdefg'
s2 = 'abcdefghijklmnopqrst'
print(obj.reverse_string(s1, 2))
print(obj.reverse_string(s1, 1))
print(obj.reverse_string(s1, 10))
print(obj.reverse_string(s2, 3))
