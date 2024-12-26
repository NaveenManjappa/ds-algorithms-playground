def find_non_repeat(my_word):
    counts = {}
    for ch in my_word:
        if ch in counts:
            counts[ch] = counts[ch]+1
        else:
            counts[ch] = 0
    for key in counts:
        if counts[key] == 0:
            return key

word = "A Green Apple"
print(find_non_repeat(word))