# Problem: Longest Substring Without Repeating Characters
# Difficulty: Medium
# Category: String
# Leetcode 3: https://leetcode.com/problems/longest-substring-without-repeating-characters/submissions/1
# Description:
"""
Given a string, find the length of the longest substring without repeating characters.
Examples:
Given "abcabcbb", the answer is "abc", which the length is 3.
Given "bbbbb", the answer is "b", with the length of 1.
Given "pwwkew", the answer is "wke", with the length of 3.
Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""


class Solution(object):
	def longest_substring(self, s):
		if not s or len(s) == 0:
			return 0
		usedChar = {}
		maxLength = 0
		start = 0
		for i in range(len(s)):
			if s[i] in usedChar and start <= usedChar[s[i]]:
				start = usedChar[s[i]] + 1
			else:
				maxLength = max(maxLength, i - start + 1)
			usedChar[s[i]] = i
		return maxLength

obj = Solution()
s1 = 'abcabcbb'
s2 = 'bbbbb'
s3 = 'pwwkew'
print(obj.longest_substring(s1), obj.longest_substring(s2), obj.longest_substring(s3))
