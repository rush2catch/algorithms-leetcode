# Problem:  Employee Importance
#  Difficulty: Easy
# Category: Array
# Leetcode 690: https://leetcode.com/problems/employee-importance/description/
# Description:
"""
You are given a data structure of employee information, which includes the employee's unique id,
his importance value and his direct subordinates' id.
For example, employee 1 is the leader of employee 2, and employee 2 is the leader of employee 3.
They have importance value 15, 10 and 5, respectively.
Then employee 1 has a data structure like [1, 15, [2]], and employee 2 has [2, 10, [3]], and employee 3 has [3, 5, []].
Note that although employee 3 is also a subordinate of employee 1, the relationship is not direct.
Now given the employee information of a company, and an employee id,
you need to return the total importance value of this employee and all his subordinates.
Example 1:
Input: [[1, 5, [2, 3]], [2, 3, []], [3, 3, []]], 1
Output: 11
Explanation:
Employee 1 has importance value 5, and he has two direct subordinates: employee 2 and employee 3.
They both have importance value 3.
"""


class Solution(object):

	def get_importance(self, employees, id):
		res = 0
		subordinates = []
		for i in range(len(employees)):
			if employees[i][0] == id:
				res += employees[i][1]
				subordinates = employees[i][2]
		for i in range(len(employees)):
			if employees[i][0] in subordinates:
				res += employees[i][1]
		return res

obj = Solution()
a1 = [[1, 5, [2, 3]], [2, 3, []], [3, 3, []]]
a2  =[[1,5,[2,3]],[2,3,[4]],[3,4,[]],[4,1,[]]]
print(obj.get_importance(a1, 1))
print(obj.get_importance(a2, 1))