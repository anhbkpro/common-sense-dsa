def arraysum(array, index=0):
    if index == len(array):
        return 0
    return array[index] + arraysum(array[index + 1: len(array)])


def arraysum1(array):
    if len(array) == 1:
        return array[0]
    return array[0] + arraysum1(array[1: len(array)])


def reverse(text):
    if len(text) == 1:
        return text[0]
    return reverse(text[1: len(text)]) + text[0]


def countX(text):
    if len(text) == 0:
        return 0
    return countX(text[1: len(text)]) + (1 if text[0] == 'x' else 0)
