from typing import Dict


def count_words(file_contents):
    words = file_contents.split()
    return len(words)


def count_characters(file_contents):
    characters = file_contents.lower()
    character_count = {}
    for char in characters:
        if char not in character_count:
            character_count[char] = 0
        character_count[char] += 1
    return character_count


def book_character_stats(character_count: Dict[str, int]):
    return sorted(
        [{"char": key, "num": value} for key, value in character_count.items()],
        key=lambda p: p["num"],
        reverse=True,
    )
