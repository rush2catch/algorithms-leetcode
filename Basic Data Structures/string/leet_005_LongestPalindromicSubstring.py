# Problem:  Longest Palindromic Substring
#  Difficulty: Medium
# Category: String
# Leetcode 5: https://leetcode.com/problems/longest-palindromic-substring/description/
# Description:
"""
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.
Example:
Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example:
Input: "cbbd"
Output: "bb"
"""


class Solution(object):
	"""
	@param: s: input string
	@return: the longest palindromic substring
	"""

	def longestPalindrome(self, s):
		# write your code here
		if not s:
			return None
		if len(s) == 0:
			return ''
		res = ''
		for i in range(len(s)):
			odd = self.helper(s, i, i)
			if len(odd) > len(res):
				res = odd
			even = self.helper(s, i, i + 1)
			if len(even) > len(res):
				res = even
		return res

	def helper(self, s, l, r):
		while l >= 0 and r < len(s) - 1 and s[l] == s[r]:
			l -= 1
			r += 1
		return s[l + 1:r]

obj = Solution()
print(obj.longestPalindrome('babad'))