def partition(left_index, right_index):
    pivot_index = right_index
    pivot = array[pivot_index]
    print(f'pivot={pivot}')
    right_index = pivot_index - 1
    while True:
        while array[left_index] < pivot:
            print(f'left: value at {left_index}: {array[left_index]}')
            left_index += 1
        while array[right_index] > pivot:
            print(f'right: value at {right_index}: {array[right_index]}')
            right_index -= 1

        if left_index > right_index:
            print(f'left_index={left_index} and right_index={right_index}')
            break
        else:
            array[left_index], array[right_index] = array[right_index], array[left_index]
    return left_index


array = [0, 5, 2, 1, 6, 3]
print(partition(0, 5))
