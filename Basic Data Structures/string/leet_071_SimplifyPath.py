# Problem: Simplify Path
# Difficulty: Medium
# Category: String
# Leetcode 71: https://leetcode.com/problems/simplify-path/description/
# Description:
"""
Given an absolute path for a file (Unix-style), simplify it.

For example,
path = "/home/", => "/home"
path = "/a/./b/../../c/", => "/c"
"""


class Solution(object):

	def simplify(self, path):

		places = [p for p in path.split('/') if p != '.' and p != '']
		stack = []

		for p in places:
			if p == '..':
				if stack:
					stack.pop()
			else:
				stack.append(p)

		return '/' + '/'.join(stack)

obj = Solution()
path = "/a/./b/////../../c/"
print(obj.simplify(path))