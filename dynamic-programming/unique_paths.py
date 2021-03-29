def unique_paths(rows, columns, memo={}):
	if rows == 1 or columns == 1:
		return 1
	key = f'{rows}{columns}'
	if key not in memo:
		memo[key] = unique_paths(rows - 1, columns, memo) + unique_paths(rows, columns - 1, memo)
	return memo[key]


print(unique_paths(6, 7, {}))
