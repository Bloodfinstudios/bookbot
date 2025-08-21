from stats import nums_of_word

def main():
    def get_book_text():
        with open("books/frankenstein.txt") as f:
            content = f.read()
            return content
    book_text = get_book_text()  
    return book_text   

book_text = main()  
word_count = nums_of_word(book_text)                   

print(f"{word_count} words found in the document")

main()

