def reverse(array):
	length = len(array) - 1
	for index, item in enumerate(array):
		if index < length/2:
			array[index], array[length - index] = array[length - index], array[index]

