# Problem:  Excel Sheet Column Number
# Difficulty: Easy
# Category: String
# Leetcode 171: https://leetcode.com/problems/excel-sheet-column-number/description/
# Description:
"""
Related to question Excel Sheet Column Title
Given a column title as appear in an Excel sheet, return its corresponding column number.
For example:
    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28
"""


class Solution(object):
	def titleToNumber(self, s):
		ans = 0
		n = len(s)
		for i in range(len(s)):
			ans += 26**i * (ord(s[n-1-i]) - ord('A') + 1)
		return ans

obj = Solution()
print(obj.titleToNumber('A'), obj.titleToNumber('AB'))