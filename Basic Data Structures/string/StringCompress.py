class Solution(object):

	def compress_string(self, s):
		count = 1
		char = s[0]
		res = []
		i = 0
		while i < len(s) - 1:
			if s[i + 1] == s[i]:
				count += 1
				i += 1
			else:
				res.append(count)
				res.append(s[i])
				i += 1
				count = 1
		res.append(count)
		res.append(s[-1])
		return res

obj = Solution()
s1 = 'aaabbcdddeeeg'
s2 = 'aaaaa'
print(obj.compress_string(s1))
print(obj.compress_string(s2))