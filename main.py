from stats import get_num_words, count_char, sorted_dictionary
import sys

# main body of the program 
def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    out_char = count_char(text)
    sort_alp_char = sorted_dictionary(out_char)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for item in sort_alp_char:
        ch = item["char"]
        num = item["num"]
        if ch.isalpha():
            print(f"{ch}: {num}")

    print("============= END ===============")


# gets book from directory
def get_book_text(path):
    with open(path) as f:
        return f.read()


main()