from stats import get_num_words, count_char

# main body of the program 
def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"Found {num_words} total words")
    out_char = count_char(text)
    print(out_char)

# gets book from directory
def get_book_text(path):
    with open(path) as f:
        return f.read()


main()