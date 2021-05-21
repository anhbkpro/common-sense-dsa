missing_hash = {}

def find_missing_number(array):
    for num in range(0, len(array)+1):
        missing_hash[num] = True

    for item in array:
        if item in missing_hash:
            missing_hash[item] = False

    for item in missing_hash:
        if missing_hash[item]:
            return item


array = [8, 2, 3, 9, 4, 7, 5, 0, 6]
print(find_missing_number(array))
