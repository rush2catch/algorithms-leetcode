# Problem: Repeated Substring Pattern
# Difficulty: Easy
# Category: String
# Leetcode 459: https://leetcode.com/problems/repeated-substring-pattern/description/
"""
Given a non-empty string check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.
You may assume the given string consists of lowercase English letters only and its length will not exceed 10000.
Example 1:
Input: "abab"
Output: True
Explanation: It's the substring "ab" twice.
Example 2:
Input: "aba"
Output: False
Example 3:
Input: "abcabcabcabc"
Output: True
Explanation: It's the substring "abc" four times. (And the substring "abcabc" twice.)
"""


class Solution(object):

	def repeated_pattern(self, s):
		if not s or len(s) == 0:
			return False
		n = 1
		while n < len(s):
			if len(s) % n == 0:
				ans = s[:n] * (len(s) // n)
				if ans == s:
					return True
			n += 1
		return False

obj = Solution()
s1 = 'abab'
s2 = 'aba'
s3 = 'abcabcabcabc'
s4 = 'aaaaaa'
print(obj.repeated_pattern(s1), obj.repeated_pattern(s2), obj.repeated_pattern(s3), obj.repeated_pattern(s4))