def triangular_number(number):
	if number == 1:
		return 1
	return number + triangular_number(number -1)


triangular_number(7)
