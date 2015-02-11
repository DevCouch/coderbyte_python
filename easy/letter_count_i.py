def letter_count(arg):
    words = arg.split(" ")
    result_word = ""
    letter_count = 0
    for word in words:
        word_map = {}
        for ch in word:
            if ch in word_map:
                word_map[ch] += 1
            else:
                word_map[ch] = 1
        max_key = max(word_map.iterkeys(), key=lambda k: word_map[k])
        if letter_count < word_map[max_key] and word_map[max_key] > 1:
            letter_count = word_map[max_key]
            result_word = word
    return result_word if letter_count > 1 else -1

print letter_count("Hello apple pie")
print letter_count("No words")
