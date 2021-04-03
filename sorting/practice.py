array = [0, 5, 2, 1, 6, 3]


def greatest_three_product(array):
    array = sorted(array)
    return array[-1] * array[-2] * array[-3]


print(greatest_three_product(array))

array = [9, 3, 2, 5, 6, 7, 1, 0, 4]


def find_missing_number(array):
    array = sorted(array)
    for index, item in enumerate(array):
        if array[index] != index:
            return index

    # If all numbers are present:
    return None


print(find_missing_number(array))


def find_greatest_number_withN(array):
    """
	This implementation is O(N) as we loop once through the array
	"""
    greatestNumberSoFar = array[0]
    for item in array:
        if item > greatestNumberSoFar:
            greatestNumberSoFar = item
    return greatestNumberSoFar


def find_greatest_number_withNlogN(array):
    """
	This implementation simply sorts the array and returns the last number.
	The sorting is O(N log N)
	"""
    array = sorted(array)
    return array[-1]


def find_greatest_number_withNexp2(array):
    for item in array:
        for value in array:
            if item <= value:
                break
        return item
	

 def max(array):
	 for item in enumerate(array):
		 itemIsGreatestNumber = True
		 for value in enumerate(array):
			if value > item:
				itemIsGreatestNumber = False
		if itemIsGreatestNumber:
			return item

print(find_greatest_number_withNexp2(array))
print(max(max(array)))