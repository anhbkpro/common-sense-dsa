def anagrams_of(string) -> []:
    if len(string) == 1:
        return [string[0]]
    collection = []
    substring_anagrams = anagrams_of(string[1:])
    for substring_anagram in substring_anagrams:
        for index in range(len(substring_anagram) + 1):
            # strings (e.g. substring_anagram) in Python are immutable -- you can't ever modify them in place, 
            # need convert the string to list and insert the character into an index
            string_list = list(substring_anagram) 
            string_list.insert(index, string[0])
            collection.append(''.join(iter(string_list))) 
    return collection


print(anagrams_of('abcd'))