def find_x(string, position=0):
    if len(string) == 0:
        return -1
    if string[position].lower() == 'x':
        return position
    else:
        return find_x(string, position + 1)


print(find_x('abcdefghijklmnopqrstuvwxyz'))
