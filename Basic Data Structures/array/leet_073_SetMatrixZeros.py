# Problem:  Set Matrix Zeros
# Difficulty: Medium
# Category: Array
# Leetcode 73: https://leetcode.com/problems/set-matrix-zeroes/description/
# Description:
"""
Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in place.
Follow up:
Did you use extra space?
A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?
"""


class Solution(object):
	def setZeroes(self, matrix):
		"""
		:type matrix: List[List[int]]
		:rtype: void Do not return anything, modify matrix in-place instead.
		"""
		col0 = 1
		rows = len(matrix)
		cols = len(matrix[0])

		for i in range(rows):
			if matrix[i][0] == 0:
				col0 = 0
			for j in range(1, cols):
				if matrix[i][j] == 0:
					matrix[i][0] = matrix[0][j] = 0

		for i in range(rows - 1, -1, -1):
			for j in range(cols - 1, 0, -1):
				if matrix[i][0] == 0 or matrix[0][j] == 0:
					matrix[i][j] = 0
			if col0 == 0:
					matrix[i][0] = 0


obj = Solution()
t1 = [[0], [1]]
obj.setZeroes(t1)
