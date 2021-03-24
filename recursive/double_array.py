def double_array(array, index):
	array[index] *= 2
	if index < len(array) - 1:
		index += 1
		double_array(array, index)


array = [1, 2, 3, 4]

double_array(array, 0)

print(array)