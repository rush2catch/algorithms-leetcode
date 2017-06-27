
"""
use a list
"""
def reverse_string(input_str):

	reversed_str = []

	if len(input_str) == 0:
		return None
	elif len(input_str) == 1:
		reversed_str = input_str
		return reversed_str
	else:
		for i in range(len(input_str)):
			buff = input_str.pop()
			reversed_str.append(buff)
		return reversed_str

# test case
test_str1 = []
test_str2 = ['a']
test_str3 = ['g', 'f', 'e', 'd', 'c', 'b', 'a']
print(reverse_string(test_str1))
print(reverse_string(test_str2))
print(reverse_string(test_str3))


"""
use a string
"""
def reverse_str(inputStr):

	reversedStr = ''
	if len(inputStr) <= 1:
		return inputStr
	else:
		for i in range(len(inputStr)):
			reversedStr += inputStr[len(inputStr) - i -1]
		return reversedStr

# test case
testStr1 = ''
testStr2 = 'a'
testStr3 = 'gfedcba'
print(reverse_str(testStr1))
print(reverse_str(testStr2))
print(reverse_str(testStr3))