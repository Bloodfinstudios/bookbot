from stats import nums_of_word
from stats import count_char
from stats import sort_list
import sys

def get_book_text(path):
    with open(path) as f:
        content = f.read()
        return content
def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    text = get_book_text(book_path)

    word_count = nums_of_word(text)
    char_text = count_char(text)
    true_list = sort_list(char_text)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...") #
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for item in true_list:
        if not item["char"].isalpha(): 
            continue
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")


