# Problem: String to Integer (atoi)
# Difficulty: Medium
# Category: String
# Leetcode 8:https://leetcode.com/problems/string-to-integer-atoi/description/
# Description:
"""
Implement atoi to convert a string to an integer.
Hint: Carefully consider all possible input cases.
If you want a challenge, please do not see below and ask yourself what are the possible input cases.
Notes: It is intended for this problem to be specified vaguely (ie, no given input specs).
You are responsible to gather all the input requirements up front.
"""


class Solution(object):
	def atoi(self, s):
		if not s or len(s) == 0:
			return None
		s.strip()
		start = 0
		sign = 1
		if s[start] == '+':
			sign = 1
			start += 1
		if s[start] == '-':
			sign = -1
			start += 1
		res = 0
		for i in range(start, len(s)):
			if ord(s[i]) - ord('0') >= 0 and ord(s[i]) - ord('9') <= 0:
				temp = ord(s[i]) - ord('0')
				res = res * 10 + temp
		return res * sign

obj = Solution()
s1 = ' +2345    6522'
s2 = '  000223'
s3 = '-99401'
print(obj.atoi(s1), obj.atoi(s2), obj.atoi(s3))