# Problem: Merge Intervals
# Difficulty: Medium
# Category: Array
# Leetcode 56:https://leetcode.com/problems/merge-intervals/description/
# Description:
"""
Given a collection of intervals, merge all overlapping intervals.

For example,
Given [1,3],[2,6],[8,10],[15,18],
return [1,6],[8,10],[15,18].
"""


class Solution(object):

	def merge(self, intervals):
		if not intervals:
			return []
		ans = []
		i = 1

		intervals.sort()
		ans.append(intervals[0])

		while i < len(intervals):
			if intervals[i][0] > ans[-1][1]:
				ans.append(intervals[i])
			if intervals[i][0] < ans[-1][1]:
				if intervals[i][1] < ans[-1][1]:
					pass
				if intervals[i][1] > ans[-1][1]:
					ans[-1][1] = intervals[i][1]
			i += 1

		return ans


obj = Solution()
intervals1 = [[1,3],[2,6],[8,10],[15,18]]
intervals2 = [[1,6], [2,5], [3, 7], [9,10], [11,15], [12,18]]
print(obj.merge(intervals1))
print(obj.merge(intervals2))