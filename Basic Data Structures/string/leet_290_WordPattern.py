# Problem:  Word Pattern
# Difficulty: Easy
# Category: String
# Leetcode 290: https://leetcode.com/problems/word-pattern/description/
# Description:
"""
Given a pattern and a string str, find if str follows the same pattern.
Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.
Examples:
pattern = "abba", str = "dog cat cat dog" should return true.
pattern = "abba", str = "dog cat cat fish" should return false.
pattern = "aaaa", str = "dog cat cat dog" should return false.
pattern = "abba", str = "dog dog dog dog" should return false.
Notes:
You may assume pattern contains only lowercase letters, and str contains lowercase letters separated by a single space.
"""


class Solution(object):
	def word_pattern(self, pattern, s):
		if not pattern and not s:
			return True
		if len(pattern) == 0 and len(s) == 0:
			return True
		arr = s.split(' ')
		dic1 = {}
		dic2 = {}
		table1 = [-1 for i in range(len(pattern))]
		table2 = [-1 for i in range(len(arr))]
		key1 = 0
		key2 = 0

		for i in range(len(pattern)):
			if pattern[i] in dic1:
				table1[i] = dic1[pattern[i]]
			else:
				dic1[pattern[i]] = key1
				table1[i] = key1
				key1 += 1

		for i in range(len(arr)):
			if arr[i] in dic2:
				table2[i] = dic2[arr[i]]
			else:
				dic2[arr[i]] = key2
				table2[i] = key2
				key2 += 1

		return table1 == table2

obj = Solution()
print(obj.word_pattern("abba", "dog cat cat dog"))
print(obj.word_pattern("abba", "dog cat cat fish"))

