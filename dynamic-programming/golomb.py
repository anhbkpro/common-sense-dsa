def golomb(n, memo={}):
	if n == 1:
		return 1
	if n not in memo:
		memo[n] = golomb(n - golomb(golomb(n-1, memo), memo), memo)
	return 1 + memo[n]


print(golomb(17))
