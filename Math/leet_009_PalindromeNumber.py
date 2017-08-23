# Problem:  Palindrome Number
# Difficulty: Easy
# Category: Math
# Leetcode 009: https://leetcode.com/problems/palindrome-number/discuss/
# Description:
"""
Determine whether an integer is a palindrome. Do this without extra space
"""


class Solution(object):

	def is_panlindrome(self, x):
		if x < 0 or (x >0 and x % 10 == 0):
			return False
		num = x
		rev = 0


		while x != 0:
			tail = x % 10
			rev = rev * 10 + tail
			x = x // 10

		return num == rev


obj = Solution()
print(obj.is_panlindrome(121))