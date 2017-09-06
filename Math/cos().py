import math
def test(A, B):
	x =0
	for i in range(len(A)):
		x += (A[i] * B[i])

	divisorA = 0
	divisorB = 0
	for i in range(len(A)):
		divisorA += (A[i] * A[i])
		divisorB += (B[i] * B[i])
	divisorA = math.sqrt(divisorA)
	divisorB = math.sqrt(divisorB)
	return x / (divisorB * divisorA)

A = [1, 4, 0]
B = [1, 2, 3]

print(test(A, B))