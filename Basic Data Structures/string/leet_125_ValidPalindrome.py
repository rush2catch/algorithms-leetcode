# Problem:  Valid Palindrome
# Difficulty: Easy
# Category: String
# Leetcode 125: https://leetcode.com/problems/valid-palindrome/#/description
# Description:
"""
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

For example,
"A man, a plan, a canal: Panama" is a palindrome.
"race a car" is not a palindrome.
"""


class Solution(object):

	def valid_palindrome(self, s):

		if len(s) == 0:
			return True

		head = 0
		tail = len(s) - 1
		isPalindrome = True

		while head <= tail and isPalindrome:
			while head <= tail and not s[head].isalpha() and not s[head].isdigit():
				head += 1
			while head <= tail and not s[tail].isalpha() and not s[tail].isdigit():
				tail -= 1
			if head <= tail and s[head].lower() != s[tail].lower():
				isPalindrome = False
			head += 1
			tail -= 1
		return isPalindrome

obj = Solution()
s1 = 'A man, a plan, a canal: Panama'
s2 = 'race a car'
s3 = 'ab'
s4 = ',.;  :[]'
s5 = 'a'
s6 = ', ..a.:'
print(obj.valid_palindrome(s1))
print(obj.valid_palindrome(s2))
print(obj.valid_palindrome(s3))
print(obj.valid_palindrome(s4))
print(obj.valid_palindrome(s5))
print(obj.valid_palindrome(s6))
