def find_non_repeat(my_word):
    counts = {}
    for ch in my_word:
        if ch in counts.keys():
            counts[ch] = counts[ch]+1
        else:
            counts[ch] = 1
    for key in counts:
        if counts[key] == 1:
            return key

word = "A Green Apple"
print(find_non_repeat(word))