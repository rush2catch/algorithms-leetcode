# Problem: Merge Sorted Array
# Difficulty: Easy
# Category: Array
# Leetcode 88: https://leetcode.com/problems/merge-sorted-array/#/description
# Description:
"""
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements
from nums2. The number of elements initialized in nums1 and nums2 are m and n respectively.
"""


class Solution(object):

	def merge(self, nums1, m, nums2, n):

		length = len(nums1)
		n = len(nums2)
		m = length - n

		while m > 0 and n > 0:
			if nums1[m - 1] > nums2[n - 1]:
				nums1[m + n - 1] = nums1[m - 1]
				m -= 1
			else:
				nums1[m + n - 1] = nums2[n - 1]
				n -= 1
		if n > 0:
			nums1[:n] = nums2[:n]

		return nums1

obj = Solution()
case1 = [1, 3, 5, 7, 9, 0, 0, 0, 0]
case2 = [2, 4, 6, 8]
print(obj.merge(case1, 5, case2, 4))