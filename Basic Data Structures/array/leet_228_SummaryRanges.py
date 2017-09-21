# Problem: Summary Ranges
# Difficulty: Medium
# Category: Array
# Leetcode 228: https://leetcode.com/problems/summary-ranges/description/
# Description:
"""
Given a sorted integer array without duplicates, return the summary of its ranges.
Example 1:
Input: [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Example 2:
Input: [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]
"""


class Solution(object):
	def summary_ranges(self, nums):
		if len(nums) == 0:
			return []
		ans = [[nums[0]]]
		for i in range(len(nums) - 1):
			if nums[i + 1] - nums[i] == 1:
				continue
			else:
				if ans[-1][-1] != nums[i]:
					ans[-1].append(nums[i])
				ans.append([nums[i + 1]])
		if nums[-1] != ans[-1][-1]:
			ans[-1].append(nums[-1])

		for i in range(len(ans)):
			if len(ans[i]) == 1:
				ans[i] = str(ans[i][0])
			else:
				ans[i] = str(ans[i][0]) + '->' + str(ans[i][1])

		return ans

obj = Solution()
arr1 = [0, 1, 2, 4, 5, 7]
arr2 = [0, 2, 3, 4, 6, 8, 9]
print(obj.summary_ranges(arr1))
print(obj.summary_ranges(arr2))