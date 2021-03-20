def insertion_sort(array):
    '''
    This version does not swap 2 values, just shift left value to the right if the value at position is larger than the temp_value  
    '''
    for index in range(1, len(array)):
        temp_value = array[index]
        position = index - 1

        print(f"Pass-through #{index}: temp_value={temp_value}")
        while position >= 0:
            # check whether the value at position is greater than the temp_value
            if array[position] > temp_value:
                # we shift that left value to the right
                array[position + 1] = array[position]
                position = position - 1
            else:
                break  # it’s time to move the temp_value into the gap
        # The final step of each pass-through is moving the temp_value into the gap
        array[position + 1] = temp_value
        print(f'after switching now the array is {array}')
    return array


print(insertion_sort([4, 2, 7, 1, 3]))
