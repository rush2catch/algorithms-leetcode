# Problem:  Implement strStr()
# Difficulty: Easy
# Category: String
# Leetcode 28: https://leetcode.com/problems/implement-strstr/#/description
# Description:
"""
Implement strStr().
Returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
"""


class Solution(object):

	def strStr(self, haystack, needle):
		"""
		:param haystack: str
		:param needle: str
		:return: int
		"""
		m = len(haystack) - len(needle)
		n = len(needle)
		if m < 0:
			return -1
		if m == 0:
			if haystack == needle:
				return 0
			else:
				return -1
		if n == 0:
			return 0
		for i in range(m + 1):
			if haystack[i:i + n] == needle:
				return i
		return -1

obj = Solution()
test_haystack = 'abcdefg'
test_needle1 = ''
test_needle2 = 'bc'
test_needle3 = 'edgq'
test_needle4 = 'abcdefghijklmn'
test_needle5 = 'abcdefg'
test_needle6 = 'abc'
test_needle7 = 'fg'
print(obj.strStr(test_haystack, test_needle1))
print(obj.strStr(test_haystack, test_needle2))
print(obj.strStr(test_haystack, test_needle3))
print(obj.strStr(test_haystack, test_needle4))
print(obj.strStr(test_haystack, test_needle5))
print(obj.strStr(test_haystack, test_needle6))
print(obj.strStr(test_haystack, test_needle7))