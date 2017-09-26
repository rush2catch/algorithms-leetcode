# Problem: House Robber
# Difficulty: Easy
# Category: Array, DP
# Leetcode 198: https://leetcode.com/problems/house-robber/description/
"""
You are a professional robber planning to rob houses along a street.
Each house has a certain amount of money stashed,
the only constraint stopping you from robbing each of them is that
adjacent houses have security system connected
and it will automatically contact the police if two adjacent houses were broken into on the same night.
Given a list of non-negative integers representing the amount of money of each house,
determine the maximum amount of money you can rob tonight without alerting the police.
"""


class Solution(object):
	def house_robber(self, nums):
		if len(nums) == 0 or not nums:
			return 0
		dp = [0 for i in range(len(nums))]
		dp[0] = nums[0]
		dp[1] = max(nums[0], nums[1])
		for i in range(2, len(nums)):
			dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])

		return dp[-1]

obj = Solution()
arr1 = [1, 3, 2, 6, 1, 4, 1]
arr2 = [1, 1, 0, 1, 2, 3, 1]
print(obj.house_robber(arr1))
print(obj.house_robber(arr2))