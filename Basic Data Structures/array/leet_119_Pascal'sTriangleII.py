# Problem:  Pascal's Triangle II
# Difficulty: Easy
# Category: Array
# Leetcode 119: https://leetcode.com/problems/pascals-triangle-ii/description/
# Description:
"""
Given an index k, return the kth row of the Pascal's triangle.

For example, given k = 3,
Return [1,3,3,1].

Note:
Could you optimize your algorithm to use only O(k) extra space?
"""


class Solution(object):

	def get_row(self, rows):
		if rows == 0:
			return [1]
		if rows == 1:
			return [1, 1]
		prev = [1, 1]
		curr = []
		for i in range(2, rows + 1):
			curr = [1] * (i + 1)
			for j in range(1, i):
				curr[j] = prev[j - 1] + prev[j]
			prev = curr
		return curr

obj = Solution()
print(obj.get_row(7))