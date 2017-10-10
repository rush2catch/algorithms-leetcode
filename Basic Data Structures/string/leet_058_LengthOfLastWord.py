# Problem: Length of Last Word
# Difficulty: Easy
# Category: String
# Leetcode 58: https://leetcode.com/problems/length-of-last-word/description/
# Description:
"""
Given a string s consists of upper/lower-case alphabets and empty space characters ' ',
return the length of last word in the string.
If the last word does not exist, return 0.
Note: A word is defined as a character sequence consists of non-space characters only.
For example,
Given s = "Hello World",
return 5.
"""


class Solution(object):
	def length_last_word(self, s):
		lo = 0
		hi = 1
		s = s.strip()
		if not s or len(s) == 0:
			return 0
		while hi < len(s):
			if s[hi - 1] == ' ' and s[hi] != ' ':
				lo = hi
			hi += 1
		return hi - lo

obj = Solution()
print(obj.length_last_word('Hello, World'))
print(obj.length_last_word('   '))