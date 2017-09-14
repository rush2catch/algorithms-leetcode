# Problem:  Reverse Vowels of a String
# Difficulty: Easy
# Category: String
# Leetcode 345: https://leetcode.com/problems/reverse-vowels-of-a-string/description/
# Description:
"""
Write a function that takes a string as input and reverse only the vowels of a string.
Example 1:
Given s = "hello", return "holle".
Example 2:
Given s = "leetcode", return "leotcede".
Note:
The vowels does not include the letter "y".
"""


class Solution(object):

	def reverseVowels(self, s):
		if not s or len(s) == 0:
			return s

		vowels = ['a', 'e', 'i', 'o', 'u']
		arr = list(s)
		left = 0
		right = len(s) - 1

		while left < right:
			while left < right and arr[left] not in vowels:
				left += 1
			while left < right and arr[right] not in vowels:
				right -= 1
			if arr[left] in vowels and arr[right] in vowels:
				arr[left], arr[right] = arr[right], arr[left]
				left += 1
				right -= 1
		return ''.join(arr)


obj = Solution()
s1 = 'hello'
s2 = 'leetcode'
print(obj.reverseVowels(s1), obj.reverseVowels(s2))