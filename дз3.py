def word_lengths(words):
    """Генератор"""
    for word in words:
        yield len(word)



words_list = ["Python", "програмування", "ітератор", "код"]

print("Довжини слів ")
for length in word_lengths(words_list):
    print(length, end=" ")
