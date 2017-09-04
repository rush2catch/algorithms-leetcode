# Problem: Rotate Image
# Difficulty: Medium
# Category: Array
# Leetcode 48: https://leetcode.com/problems/rotate-image/description/
# Description:
"""
You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Note:
You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

Example 1:

Given input matrix =
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],

rotate the input matrix in-place such that it becomes:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]
Example 2:

Given input matrix =
[
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
],

rotate the input matrix in-place such that it becomes:
[
  [15,13, 2, 5],
  [14, 3, 4, 1],
  [12, 6, 8, 9],
  [16, 7,10,11]
]

"""


class Solution(object):

	def rotate_image(self, matrix):
		if not matrix:
			return matrix
		self.up_down_rotate(matrix)
		print(matrix)
		self.sysmetric_rotate(matrix)
		print(matrix)

	def up_down_rotate(self, matrix):
		n = len(matrix)
		rowUp = 0
		rowDown = len(matrix) - 1
		while rowUp < rowDown:
			for i in range(n):
				matrix[rowUp][i], matrix[rowDown][i] = matrix[rowDown][i], matrix[rowUp][i]
			rowUp += 1
			rowDown -= 1

	def sysmetric_rotate(self, matrix):
		n = len(matrix)
		for i in range(n):
			for j in range(i, n):
				matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


obj = Solution()
matrix = [[1,2,3], [4,5,6], [7,8,9]]
obj.rotate_image(matrix)