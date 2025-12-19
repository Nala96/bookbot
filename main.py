import sys
from stats import (character_count, word_count, sorted_chars)

def get_book_text(book_1):
    with open(book_1) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    text = get_book_text(book_path)
    words = word_count(text)
    c_count = character_count(text)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {words} total words")
    print("--------- Character Count -------")

    sorted_list = sorted_chars(c_count)
    for item in sorted_list:
        ch = item["char"]
        if ch.isalpha():
            print(f"{ch}: {item['num']}")

    print("============= END ===============")

main()
