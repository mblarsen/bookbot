import sys

from stats import book_character_stats, count_characters, count_words


def get_book_text(path):
    with open(path) as f:
        return f.read()


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    book_text = get_book_text(book_path)

    num_words = count_words(book_text)
    # print(f"{num_words} words found in the document")

    character_count = count_characters(book_text)
    # print(character_count)

    book_stats = book_character_stats(character_count)
    print(f"""============ BOOKBOT ============
Analyzing book found at {book_path}
----------- Word Count ----------
Found {num_words} total words
--------- Character Count -------""")
    for word_count in book_stats:
        if word_count["char"].isalpha():
            char = word_count["char"]
            num = word_count["num"]
            print(f"{char}: {num}")
    print("============= END ===============")
