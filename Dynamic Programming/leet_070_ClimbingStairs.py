# Problem: Climbing Stairs
# Difficulty: Easy
# Category: Array/DP
# Leetcode 70: https://leetcode.com/problems/climbing-stairs/description/
# Description:
"""
You are climbing a stair case. It takes n steps to reach to the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
Note: Given n will be a positive integer.
"""


class Solution(object):
	def climb_stairs(self, n):
		if n == 1:
			return 1
		if n == 2:
			return 2
		dp = [0 for i in range(n)]
		dp[0] = 1
		dp[1] = 2
		for i in range(2, n):
			dp[i] = dp[i-1] + dp[i-2]
		return dp[-1]

obj = Solution()
print(obj.climb_stairs(10))