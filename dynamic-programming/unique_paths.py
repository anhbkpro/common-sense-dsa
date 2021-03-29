def unique_paths(rows, columns, memo={}):
	if rows == 1 or columns == 1:
		return 1
	if f'{rows}{columns}' not in memo:
		memo[f'{rows}{columns}'] = unique_paths(rows - 1, columns, memo) + unique_paths(rows, columns - 1, memo)
	return memo[f'{rows}{columns}']


print(unique_paths(6, 7, {}))
