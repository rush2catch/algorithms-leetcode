# Problem:  Add Binary
# Difficulty: Easy
# Category: String
# Leetcode 67: https://leetcode.com/problems/add-binary/#/description
# Description:
"""
Given two binary strings, return their sum (also a binary string).

For example,
a = "11"
b = "1"
Return "100".
"""


class Solution(object):

	def add_binary(self, a, b):

		indexa = len(a) - 1
		indexb = len(b) - 1
		carry = 0
		res = ''

		while indexa >= 0 or indexb >= 0:
			if indexa >= 0:
				x = int(a[indexa])
			else:
				x = 0
			if indexb >= 0:
				y = int(b[indexb])
			else:
				y = 0
			if (x + y + carry) % 2 == 0:
				res = '0' + res
			else:
				res = '1' + res
			carry = (x + y + carry) // 2
			indexa -= 1
			indexb -= 1
		if carry == 1:
			res = '1' + res
		return res


obj = Solution()
a1 = '0000'
a2 = '1010'
a3 = '1111'
b1 = '0001'
b2 = '101'
b3 = '10'
b4 = '11'
print("result should be: '0001', res = {}".format(obj.add_binary(a1, b1)))
print("result should be: '1011', res = {}".format(obj.add_binary(a2, b1)))
print("result should be: '1101', res = {}".format(obj.add_binary(a2, b4)))
print("result should be: '10001', res = {}".format(obj.add_binary(a3, b3)))
print("result should be: '11110', res = {}".format(obj.add_binary(a3, a3)))
