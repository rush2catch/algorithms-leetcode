# Problem:  Reverse Words in a String III
# Difficulty: Easy
# Category: String
# Leetcode 557: https://leetcode.com/problems/reverse-words-in-a-string-iii/#/description
# Description:
"""
Given a string, you need to reverse the order of characters in each word within a sentence
while still preserving whitespace and initial word order.
Example 1:
Input: "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
Note: In the string, each word is separated by single space and there will not be any extra space in the string.
"""


class Solution(object):

	def reverse_word(self, s):
		low = 0
		high = 1
		res = ''
		while high < len(s):
			if s[high] == ' ':
				res += s[low:high][::-1]
				res += ' '
				low = high + 1
				high = low + 1
			elif high == len(s) - 1:
				res += s[low:high][::-1]
				high += 1
			else:
				high += 1
		return res

obj = Solution()
s1 = 'Let\'s take Leetcode contest'
print(obj.reverse_word(s1))
