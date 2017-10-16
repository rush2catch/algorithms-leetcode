# Problem: Group Anagrams
# Difficulty: Medium
# Category: String
# Leetcode 49: https://leetcode.com/problems/group-anagrams/description/
# Description:
"""
Given an array of strings, group anagrams together.
For example, given: ["eat", "tea", "tan", "ate", "nat", "bat"],
Return:
[
  ["ate", "eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note: All inputs will be in lower-case.
"""


class Solution(object):

	def group_anagrams(self, strs):
		if not strs:
			return []
		dic = {}
		ans = []
		for s in strs:
			temp = ''.join(sorted(s))
			if temp in dic:
				dic[temp].append(s)
			else:
				dic[temp] = [s]
		for key in dic:
			ans.append(dic[key])
		return ans

	def group_anagram(self, strs):
		if not strs:
			return []
		dic = {}
		ans = []
		index = 0
		for i in range(len(strs)):
			s = ''.join(sorted(strs[i]))
			if s in dic:
				ans[dic[s]].append(strs[i])
			else:
				dic[s] = index
				ans.append([strs[i]])
				index += 1
		return ans

obj = Solution()
str1 = ['eat', 'eta', 'ate', 'aet', 'pen', 'epn', 'number', 'call', 'llac']
print(obj.group_anagram(str1))
