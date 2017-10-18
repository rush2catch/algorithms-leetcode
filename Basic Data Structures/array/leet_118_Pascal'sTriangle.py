# Problem:  Pascal's Triangle
# Difficulty: Easy
# Category: Array
# Leetcode 118: https://leetcode.com/problems/pascals-triangle/description/
# Description:
"""
Given numRows, generate the first numRows of Pascal's triangle.

For example, given numRows = 5,
Return

[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
"""


class Solution(object):

	def generate(self, rows):
		res = []
		for i in range(rows):
			res.append([1] * (i + 1))
			if i > 1:
				for j in range(1, i):
					res[i][j] = res[i-1][j-1] + res[i-1][j]
		return res

obj = Solution()
print(obj.generate(5))
