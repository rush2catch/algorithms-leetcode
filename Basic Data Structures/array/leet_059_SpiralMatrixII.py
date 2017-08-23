# Problem:  Spiral Matrix II
# Difficulty: Medium
# Category: Array
# Leetcode 59: https://leetcode.com/problems/spiral-matrix-ii/description/
# Description:
"""
Given an integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

For example,
Given n = 3,

You should return the following matrix:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]

"""


class Solution(object):

	def generateMatrix(self, n):

		matrix = [ ([0] * n) for i in range(n)]

		if n == 0:
			return matrix

		rowStart = 0
		rowEnd = n - 1
		colStart = 0
		colEnd = n - 1

		val = 1

		while rowStart <= rowEnd and colStart <= colEnd:

			for i in range(colStart, colEnd + 1):
				matrix[rowStart][i] = val
				val += 1
			rowStart += 1

			for i in range(rowStart, rowEnd + 1):
				matrix[i][colEnd] = val
				val += 1
			colEnd -= 1

			if rowStart <= rowEnd:
				for i in range(colEnd, colStart - 1, -1):
					matrix[rowEnd][i] = val
					val += 1
			rowEnd -= 1

			if colStart <= colEnd:
				for i in range(rowEnd, rowStart - 1, -1):
					matrix[i][colStart] = val
					val += 1
			colStart += 1

		return matrix


obj = Solution()
print(obj.generateMatrix(2))
print(obj.generateMatrix(3))
print(obj.generateMatrix(4))
