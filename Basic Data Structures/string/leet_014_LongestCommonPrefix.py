# Problem: Longest Common Prefix
# Difficulty: Easy
# Category: String
# Leetcode 14: https://leetcode.com/problems/longest-common-prefix/description/
# Description:
"""
Write a function to find the longest common prefix string amongst an array of strings.
"""


class Solution(object):

	def commonprefix(self, strs):
		if not strs:
			return ''
		if len(strs) == 1:
			return strs[0]


		while len(strs) > 1:
			tempStr = self.prefix(strs[0], strs[1])
			strs.pop(0)
			strs.pop(0)
			strs.insert(0, tempStr)
		return strs[0]


	def prefix(self, s1, s2):
		if not s1 or not s2:
			return ''
		n1 = len(s1)
		n2 = len(s2)
		n = min(n1, n2)
		i = 0
		for i in range(n):
			if s1[i] != s2[i]:
				return s1[:i]
		return s1


obj = Solution()
A = ["ABCDEFG","ABCEFG","ABCEFA"]
B = ["ABCDEFG","ABCDEFG","ABCDEFG"]
print(obj.commonprefix(B))
#print(obj.prefix(B[0], B[1]))