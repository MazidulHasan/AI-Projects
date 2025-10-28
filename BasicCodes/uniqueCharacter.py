def first_unique_char(s:str) -> str:
    char_count = {}
    
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1
    
    for char in s:
        if char_count[char] == 1:
            return char
    # print(type(2.2))
    return 2.2

print(first_unique_char("aabbcdd"))
print(first_unique_char("aabbccdd"))