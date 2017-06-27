def reverse_string(input_str):

	reversed_string = []

	if len(input_str) == 0:
		return None
	elif len(input_str) == 1:
		reversed_string = input_str
		return reversed_string
	else:
		for i in range(len(input_str)):
			buff = input_str.pop()
			reversed_string.append(buff)
		return reversed_string


test_str1 = []
test_str2 = ['a']
test_str3 = ['g', 'f', 'e', 'd', 'c', 'b', 'a']
print(reverse_string(test_str1))
print(reverse_string(test_str2))
print(reverse_string(test_str3))
