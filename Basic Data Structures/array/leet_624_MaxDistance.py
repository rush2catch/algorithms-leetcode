# Problem:  Maximum Distance in Arrays
# Difficulty: Easy
# Category: Array
# Leetcode 624: https://leetcode.com/problems/maximum-distance-in-arrays/#/description
# Description:
"""
Given m arrays, and each array is sorted in ascending order.
Now you can pick up two integers from two different arrays (each array picks one) and calculate the distance.
We define the distance between two integers a and b to be their absolute difference |a-b|.
Your task is to find the maximum distance.

Example 1:
Input:
[[1,2,3],
 [4,5],
 [1,2,3]]
Output: 4
Explanation:
One way to reach the maximum distance 4 is to pick 1 in the first or third array and pick 5 in the second array.
Note:
Each given array will have at least 1 number. There will be at least two non-empty arrays.
The total number of the integers in all the m arrays will be in the range of [2, 10000].
The integers in the m arrays will be in the range of [-10000, 10000].
"""


class Solution(object):
	def max_distance(self, arrays):
		# initialize
		minimum = 10000
		maximum = -10000

		for i in range(len(arrays)):
			if len(arrays[i]) == 1:
				if arrays[i][0] <= minimum:
					minimum = arrays[i][0]
				if arrays[i][0] >= maximum:
					maximum = arrays[i][0]
			else:
				if arrays[i][0] <= minimum:
					minimum = arrays[i][0]
				if arrays[i][len(arrays[i]) - 1] >= maximum:
					maximum = arrays[i][len(arrays[i]) - 1]

		return maximum - minimum

obj = Solution()
test_case1 = [[1, 2, 3], [4, 5], [1, 2, 3]]
test_case2 = [[1], [1]]
print(obj.max_distance(test_case1))
print(obj.max_distance(test_case2))