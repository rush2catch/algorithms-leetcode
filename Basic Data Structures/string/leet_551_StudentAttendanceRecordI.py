# Problem:  Student Attendance Record I
# Difficulty: Easy
# Category: String
# Leetcode 551: https://leetcode.com/problems/student-attendance-record-i/#/description
# Description:
"""
You are given a string representing an attendance record for a student.
The record only contains the following three characters:
'A' : Absent.
'L' : Late.
'P' : Present.
A student could be rewarded if his attendance record doesn't contain
more than one 'A' (absent) or more than two continuous 'L' (late).
You need to return whether the student could be rewarded according to his attendance record.
Example 1:
Input: "PPALLP"
Output: True
Example 2:
Input: "PPALLL"
Output: False
"""


class Solution(object):

	def check_record(self, s):
		absent = True
		late = True
		abscn = 0
		i = 0
		while i < len(s) and absent and late:
			if abscn > 1:
				absent = False
			if s[i] == 'A':
				abscn += 1
			if s[i] == 'L' and i + 3 <= len(s) and set(s[i:i+3]) == {'L'}:
				late = False
			i += 1
		if abscn > 1:
			absent = False
		return absent and late

obj = Solution()
s1 = 'PPALLP'
s2 = 'PPALLL'
s3 = 'ALLLPPPLLPL'
s4 = 'AA'
print(obj.check_record(s1))
print(obj.check_record(s2))
print(obj.check_record(s3))
print(obj.check_record(s4))
