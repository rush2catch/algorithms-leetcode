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

		maxLength = 0
		maxSub = ''

		for i in range(len(s) + 1):
			for j in range(len(s) + 1):
				sub = s[i:j]
				if self.isPalindrome(sub) and len(sub) > maxLength:
					maxSub = sub
					maxLength = len(sub)
		return maxSub

	def isPalindrome(self, s):
		if not s or len(s) == 0:
			return True

		low = 0
		high = len(s) - 1

		while low <= high:
			if s[low] != s[high]:
				return False
			else:
				low += 1
				high -= 1

		return True


obj = Solution()
print(obj.longestPalindrome('babad'))