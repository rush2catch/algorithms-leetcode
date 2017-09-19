# Problem: Longest Palindrome
# Difficulty: Easy
# Category: String
# Leetcode 409: https://leetcode.com/problems/longest-palindrome/description/
# Description:
"""
Given a string which consists of lowercase or uppercase letters,
find the length of the longest palindromes that can be built with those letters.
This is case sensitive, for example "Aa" is not considered a palindrome here.
Note:
Assume the length of given string will not exceed 1,010.
Example:
Input:
"abccccdd"
Output:
7
Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.
"""


class Solution(object):

	# two-pass solution
	def longestPalindrome(self, s):
		if not s or len(s) == 0:
			return 0
		table = [0 for _ in range(58)]
		count = 0
		for c in s:
			table[ord(c) - ord('A')] += 1
		for num in table:
			count += num // 2
		return 2*count + min(1, len(s)-2*count)

	# one-pass solution
	def palindromeLength(self, s):
		if not s or len(s) == 0:
			return 0
		table = [0 for _ in range(58)]
		count = 0
		for c in s:
			if table[ord(c) - ord('A')] == 1:
				table[ord(c) - ord('A')] -= 1
				count += 2
			elif table[ord(c) - ord('A')] == 0:
				table[ord(c) - ord('A')] += 1
		return count + min(1, len(s) - count)

obj = Solution()
s1 = "abccccdd"
s2 = 'a'
s3 = 'ABabedDDAD'
s4 = 'aabbccddeeffgggwerrtuimn'
print(obj.longestPalindrome(s1), obj.longestPalindrome(s2), obj.longestPalindrome(s3))
print(obj.palindromeLength(s1), obj.palindromeLength(s2), obj.palindromeLength(s3))
