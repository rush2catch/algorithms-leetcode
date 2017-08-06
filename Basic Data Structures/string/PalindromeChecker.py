class Solution(object):

	def palindrome_checker(self, s):

		if len(s) == 0:
			return True

		head = 0
		tail = len(s) - 1
		isPalindrome = True

		while head <= tail and isPalindrome:
			if s[head] == s[tail]:
				head += 1
				tail -= 1
			else:
				isPalindrome = False

		return isPalindrome

obj = Solution()
s1 = ''
s2 = 'a'
s3 = 'abcdedcba'
s4 = 'aaaaa'
s5 = 'abeddergtw'
print(obj.palindrome_checker(s1))
print(obj.palindrome_checker(s2))
print(obj.palindrome_checker(s3))
print(obj.palindrome_checker(s4))
print(obj.palindrome_checker(s5))