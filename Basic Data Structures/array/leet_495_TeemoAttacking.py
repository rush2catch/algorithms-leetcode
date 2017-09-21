# Problem: Teemo Attacking
# Difficulty: Medium
# Category: Array
# Leetcode 495: https://leetcode.com/problems/teemo-attacking/description/


class Solution(object):
	def teemo(self, timeSeries, duration):
		for i in range(len(timeSeries)):
			timeSeries[i] = [timeSeries[i], timeSeries[i] + duration - 1]
		interval = [timeSeries[0]]
		i = 1
		ans = 0

		while i < len(timeSeries):
			if interval[-1][1] < timeSeries[i][0]:
				interval.append(timeSeries[i])
			else:
				if interval[-1][1] < timeSeries[i][1]:
					interval[-1][1] = timeSeries[i][1]
			i += 1

		for i in range(len(interval)):
			ans += interval[i][1] - interval[i][0] + 1

		return ans

obj = Solution()
time1 = [1, 4]
time2 = [1, 2]
time3 = [1, 2, 3, 4, 5]
print(obj.teemo(time1, 2))
print(obj.teemo(time2, 2))
print(obj.teemo(time3, 7))