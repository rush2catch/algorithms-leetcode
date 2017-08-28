# Problem:  Reverse Words in a String
# Difficulty: Medium
# Category: String
# Leetcode 151: https://leetcode.com/problems/reverse-words-in-a-string/description/
# Description:
"""
Given an input string, reverse the string word by word.

For example,
Given s = "the sky is blue",
return "blue is sky the".
"""


class Solution(object):

	def reverse_words(self, s):
		if len(s) == 0:
			return s

		low = 0
		high = 0
		res = ''

		while high < len(s):
			if s[high] == ' ':
				if s[low] != ' ':
					res += self.reverse(s[low:high])
					low = high


			if s[high] != ' ':
				if s[low] == ' ':
					res += s[low:high]
					low = high

			high += 1



		res += self.reverse(s[low:high])

		res = self.reverse(res)

		return res

	def reverse(self, s):
		if len(s) == 0:
			return s
		low = 0
		high = len(s) - 1
		arr = list(s)
		while low <= high:
			arr[low], arr[high] = arr[high], arr[low]
			low += 1
			high -= 1
		return ''.join(arr)



obj = Solution()
str1 = '   the sky   is blue'
print(obj.reverse_words('   the sky   is blue'))
print(obj.reverse_words('the    sky is blue   '))