def add_until_100(array):
    if len(array) == 0:
        return 0
    remaining_sum = add_until_100(array[1:])
    if array[0] + remaining_sum > 100:
        return remaining_sum
    else:
        return array[0] + remaining_sum


print(add_until_100([30, 20, 60, 10, 50]))
