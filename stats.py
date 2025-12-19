def word_count(book_1):
    words = book_1.split()
    return len(words)

def character_count(book_1):
    char_count = {}
    for char in book_1:
        char_lower = char.lower()
        if char_lower in char_count:
            char_count[char_lower] += 1
        else:
            char_count[char_lower] = 1
    return char_count

def sorting(char):
    return char["num"]

def sorted_chars(char_count_dict):
    char_list = []
    for ch, num in char_count_dict.items():
        one_char = {
            "char": ch,
            "num": num,
        }
        char_list.append(one_char)

    char_list.sort(reverse=True, key=sorting)
    return char_list
