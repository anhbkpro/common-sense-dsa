def even_count(array):
    collection = []
    if len(array) == 0:
        return []
    else:
        if array[0] % 2 == 0:
            collection.append(array[0])
        collection.extend(even_count(array[1:]))
    return collection


print(even_count([1, 2, 3, 4]))
