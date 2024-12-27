def find_first_repeated_char(my_word):
    keys = set()
    for ch in my_word:
        if ch in keys:
            return ch
        keys.add(ch)



my_string = "green apple"
print(find_first_repeated_char(my_string))