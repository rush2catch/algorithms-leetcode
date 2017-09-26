# Problem: Multiply Strings
# Difficulty: Medium
# Category: String
# Leetcode 43: https://leetcode.com/problems/multiply-strings/description/
"""
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2.
Note:
The length of both num1 and num2 is < 110.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.
"""


class Solution(object):

	def multiply(self, num1, num2):
		if num1 == '0' or num2 == '0':
			return '0'
		ans = 0
		res = ''
		for i in range(len(num1) - 1, -1, -1):
			for j in range(len(num2) - 1, -1, -1):
				ans += ((ord(num1[i]) - ord('0')) * (10**(len(num1) - i - 1))) * \
					   ((ord(num2[j]) - ord('0')) * (10**(len(num2) - j -1)))
		while ans != 0:
			res = str(ans % 10) + res
			ans = ans // 10
		return res

obj = Solution()
print(obj.multiply('23', '17'))
print(obj.multiply('99', '99'))
print(obj.multiply('100', '111111113445012'))