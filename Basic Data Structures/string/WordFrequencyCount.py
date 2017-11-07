class Solution(object):

	def word_frequency(self,s):
		if not s or len(s) == 0:
			return ''
		arr = s.split()
		wordFrequency = {}
		for word in arr:
			wordFrequency[word] = wordFrequency.get(word, 0) + 1
		maxCount = 0
		secCount = 0
		for key in wordFrequency:
			if wordFrequency[key] > maxCount:
				secCount = maxCount
				maxCount = wordFrequency[key]
			elif wordFrequency[key] < maxCount and wordFrequency[key] > secCount:
				secCount = wordFrequency[key]

		ans = []
		for key in wordFrequency:
			if wordFrequency[key] == secCount:
				ans.append(key)
		return ans

obj = Solution()
s1 = 'apple apple apple one one two two three three three four'
print(obj.word_frequency(s1))