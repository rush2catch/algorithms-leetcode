def fac(n):
	if n == 0:
		return 1
	if n == 1:
		return 1
	return n*fac(n-1)

def fac_dp(n):
	dp = [1 for i in range(n+1)]
	for i in range(1, n+1):
		dp[i] = dp[i-1]*i
	return dp[-1]


def print_fac(n):
	for i in range(n+1):
		print(i, fac(i))
	for i in range(n+1):
		print(i, fac_dp(i))

print_fac(5)