def get_book_text(file_path):
    with open(file_path, encoding="utf-8") as f:
        file_contents = f.read()
    return file_contents

def get_total_word_count(file_path):
    text = get_book_text(file_path)
    words = text.split()
    return len(words)

def get_char_count(file_path) -> dict[str, int]:
    text = get_book_text(file_path).lower()
    char_count = {}
    for char in text:
        if char.isalpha():
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    return char_count

def sort_on(char: tuple[str, int]) -> int:
    return char[1]

def chars_dict_to_sorted_list(char_count: dict[str, int]) -> list[tuple[str, int]]:
    sorted_char_list = []
    for char, count in char_count.items():
        sorted_char_list.append((char, count))
    sorted_char_list.sort(reverse=True, key=sort_on)
    return sorted_char_list

