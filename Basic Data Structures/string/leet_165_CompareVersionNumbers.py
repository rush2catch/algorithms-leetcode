# Problem: Compare Version Numbers
# Difficulty: Medium
# Category: String
# Leetcode 165: https://leetcode.com/problems/compare-version-numbers/description/
"""
Compare two version numbers version1 and version2.
If version1 > version2 return 1, if version1 < version2 return -1, otherwise return 0.

You may assume that the version strings are non-empty and contain only digits and the . character.
The . character does not represent a decimal point and is used to separate number sequences.
For instance, 2.5 is not "two and a half" or "half way to version three",
it is the fifth second-level revision of the second first-level revision.

Here is an example of version numbers ordering:

0.1 < 1.1 < 1.2 < 13.37
"""


class Solution(object):

	def compare_version(self, version1, version2):
		ver1 = [int(i) for i in version1.split('.')]
		ver2 = [int(i) for i in version2.split('.')]
		length = max(len(ver1), len(ver2))
		for i in range(length):
			v1 = ver1[i] if i < len(ver1) else 0
			v2 = ver2[i] if i < len(ver2) else 0
			if v1 > v2:
				return 1
			if v1 < v2:
				return -1

		return 0

obj = Solution()
v1 = '0.1.001.3'
v2 = '1.3.043.1'
v3 = '0.1.001.3'
print(obj.compare_version(v1, v2))
print(obj.compare_version(v1, v3))