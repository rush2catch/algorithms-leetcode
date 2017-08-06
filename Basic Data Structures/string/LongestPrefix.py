class Solution(object):
	def prefix(self, s1, s2):
		if len(s1) == 0 or len(s2) == 0:
			return None
		n = min(len(s1), len(s2))
		i = 1
		while i <= n:
			if s1[:i] == s2[:i]:
				i += 1
			else:
				return s1[:i - 1]
		return s1

obj = Solution()
s1 = 'abceeeee'
s2 = 'abcd'
s3 = 'a'
s4 = 'b'
s5 = ''
print(obj.prefix(s1, s2))
print(obj.prefix(s3, s3))
print(obj.prefix(s3, s4))
print(obj.prefix(s4, s5))