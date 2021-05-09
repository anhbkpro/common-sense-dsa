def reverse(array):
	array_length = len(array) - 1
	for index, item in enumerate(array):
		if index < array_length/2:
			temp = item
			item = array[array_length-index]
			print(item)
			array[array_length-index] = temp
			array[index] = item
			print(f'assign {item} to item at {index}')
			print(array[index])
