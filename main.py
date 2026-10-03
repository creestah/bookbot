import sys
from stats import get_char_count, get_total_word_count, chars_dict_to_sorted_list

# Void Method 
# def print_report(file_path: str, word_count: int, char_count: dict[str, int]):
#     word_count = get_total_word_count(file_path)
#     char_count = get_char_count(file_path)
#     print(f"============ BOOKBOT ============\nAnalyzing book found at {file_path}...")
#     print(f"----------- Word Count ----------\nFound {word_count} total words.")    
#     for char, count in chars_dict_to_sorted_list(char_count):
#         print(f"{char}: {count}")
#     print("============= END ===============")

def print_report(file_path: str, word_count: int, char_count: dict[str, int]) -> str:
    word_count = get_total_word_count(file_path)
    char_count = get_char_count(file_path)

    result = ""
    result += f"============ BOOKBOT ============\nAnalyzing book found at {file_path}..." + f"\n----------- Word Count ----------\nFound {word_count} total words."
    for char, count in chars_dict_to_sorted_list(char_count):
        result += f"\n{char}: {count}"
    result += f"\n============= END ==============="
    return result
    
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
        
    FILE_PATH = sys.argv[1]
    word_count = get_total_word_count(FILE_PATH)
    char_count = get_char_count(FILE_PATH)
    # print_report(FILE_PATH, word_count, char_count)
    print(print_report(FILE_PATH, word_count, char_count))

if __name__ == "__main__":
    main()
