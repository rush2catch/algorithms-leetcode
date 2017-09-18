def fac(n):
	if n == 0:
		return 1
	if n == 1:
		return 1
	return n*fac(n-1)

def print_fac(n):
	for i in range(n+1):
		print(i, fac(i))

print_fac(50)