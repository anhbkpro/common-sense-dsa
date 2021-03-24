def double_array(array, index=0):
    # Base case: when the index goes past the end of the array
    if index >= len(array):
        return

    array[index]*=2
    double_array(array, index + 1)


array = [1, 2, 3, 4]
double_array(array, 0)
print(array)
