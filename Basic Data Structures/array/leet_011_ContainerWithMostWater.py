# Problem: Container With Most Water
# Difficulty: Medium
# Category: Array
# Leetcode 11: https://leetcode.com/problems/container-with-most-water/description/
# Description:
"""
Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai).
n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines,
which together with x-axis forms a container, such that the container contains the most water.
Note: You may not slant the container and n is at least 2.
"""


class Solution(object):
	def max_area(self, heights):
		low = 0
		high = len(heights) - 1
		area = 0
		max_area = 0
		while low < high:
			length = high - low
			height = min(heights[low], heights[high])
			area = length * height
			max_area = max(max_area, area)
			if heights[low] < heights[high]:
				low += 1
			else:
				high -= 1
		return max_area

obj = Solution()
a1 = [1, 2, 3, 4, 5, 6]
a2 = [4, 1, 5, 2, 9, 2, 1]
print(obj.max_area(a1), obj.max_area(a2))