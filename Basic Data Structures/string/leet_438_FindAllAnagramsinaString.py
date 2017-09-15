# Problem: Find All Anagrams in a String
# Difficulty: Easy
# Category: String
# Leetcode 438: https://leetcode.com/problems/find-all-anagrams-in-a-string/discuss/
# Description:
"""
Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.
Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.
The order of output does not matter.
Example 1:
Input:
s: "cbaebabacd" p: "abc"
Output:
[0, 6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
"""


class Solution(object):
	def find_anagrams(self, s, p):
		n = len(p)
		ans = []

		for i in range(len(s) - n + 1):
			if sorted(s[i:n+i].lower()) == sorted(p.lower()):
				ans.append(i)
		return ans

obj = Solution()
s1 = "cbaebabacd"
p1 = "abc"
s2 = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
p2 = 'a'
print(obj.find_anagrams(s1, p1))
print(obj.find_anagrams(s2, p2))