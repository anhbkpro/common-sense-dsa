def insertion_sort(array):
    for i in range(1, len(array)):
        temp_value = array[i]
        print(f"Pass-though #{i}: temp_value={temp_value}")
        # if i - 1 >= 0 and array[i-1] > temp_value:
        #     array[i] = array[i-1]
        for j in range(i):
            if i-j-1 >= 0 and array[i-j-1] > temp_value:
                array[i-j], array[i-j-1] = array[i-j-1], array[i-j]
                print(f'after switching now the array is {array}')


print(insertion_sort([4, 2, 7, 1, 3]))
