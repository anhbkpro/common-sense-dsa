def reverse(array):
	for index in range(0, len(array)//2):
		array[index], array[(len(array)-1)-index] = array[(len(array)-1)-index], array[index]
