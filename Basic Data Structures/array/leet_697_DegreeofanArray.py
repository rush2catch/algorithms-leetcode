# Problem: Degree of an Array
# Difficulty: Easy
# Category: Array/Hash Table
# Leetcode 697: https://leetcode.com/problems/degree-of-an-array/description/
# Description:
"""
Given a non-empty array of non-negative integers nums,
the degree of this array is defined as the maximum frequency of any one of its elements.
Your task is to find the smallest possible length of a (contiguous) sub array of nums, that has the same degree as nums.
Example 1:
Input: [1, 2, 2, 3, 1]
Output: 2
Explanation:
The input array has a degree of 2 because both elements 1 and 2 appear twice.
Of the sub arrays that have the same degree:
[1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
The shortest length is 2. So return 2.
Example 2:
Input: [1,2,2,3,1,4,2]
Output: 6
"""

class Solution(object):

	def degree(self, nums):
		left, right, count = {}, {}, {}
		for i, x in enumerate(nums):
			if x not in left:
				left[x] = i
			right[x] = i
			if x not in count:
				count[x] = 1
			else:
				count[x] += 1

		ans = len(nums)
		degree = max(count.values())
		for x in count:
			if count[x] == degree:
				ans = min(ans, right[x]-left[x]+1)
		return ans

obj = Solution()
a1 = [1, 2, 2, 3, 1]
a2 = [1,2,2,3,1,4,2]
print(obj.degree(a1), obj.degree(a2))

