# Problem:  Reverse String
# Difficulty: Easy
# Category: String
# Leetcode 344: https://leetcode.com/problems/reverse-string/#/description
# Description:
"""
Write a function that takes a string as input and returns the string reversed.
Example:
Given s = "hello", return "olleh".
"""


class Solution(object):

	def reverse_string_1(self, s):
		if not s:
			return s
		result = ''
		for i in range(len(s) - 1, -1, -1):
			result += s[i]
		return result

	def reverse_string_2(self, s):
		return s[::-1]

obj = Solution()
test_1 = 'hello'
test_2 = 'gsterssh5e'
print(obj.reverse_string_1(test_1))
print(obj.reverse_string_2(test_1))
print(obj.reverse_string_1(test_2))
print(obj.reverse_string_1(test_2))
