class Solution(object):
	def valid(self, s):
		s = s.strip()
		i = 0
		dotCount = 0
		if s[0] == '+' or s[0] == '-':
			i += 1
		while i < len(s):
			if i == 1 and s[i] == '.' and (s[0] == '+' or s[0] == '-'):
				return False
			elif dotCount > 1:
				return False
			elif s[i] == '.':
				dotCount += 1
				i += 1
			elif ord(s[i]) - ord('0') < 0 or ord(s[i]) - ord('9') > 0:
				return False
			else:
				i += 1
		if dotCount > 1:
			return False
		else:
			return True

obj = Solution()
s1 = '+0.  1'
s2 = '+.01'
s3 = 'abd'
print(obj.valid(s1), obj.valid(s2), obj.valid(s3))
