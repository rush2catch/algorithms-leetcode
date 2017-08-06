"""
Yelp Technical Question v8
出现连续多个字符的时候,只保留一个字符.
比如"adheeeekee" -> "adheke".
"""


class Solution(object):

	def letter_del(self, s):
		res = ''
		low = 0
		high = 1

		if len(s) == 0:
			return s
		while high < len(s):
			if s[low] == s[high]:
				high += 1
			else:
				res += s[low]
				low = high
				high = low + 1
		res += s[len(s) - 1]
		return  res

obj = Solution()
s1 = 'adheeeekee'
s2 = 'aaaaabcdeeefgkkkeddsseeseeeeewwwww'
s3 = 'aaabbbccccddddeeefffghkj'
print(obj.letter_del(s1))
print(obj.letter_del(s2))
print(obj.letter_del(s3))