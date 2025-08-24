from stats import nums_of_word
from stats import count_char
from stats import sort_list

def main():
    # This is the main body of my text
    def get_book_text():
        with open("books/frankenstein.txt") as f:
            content = f.read()
            return content
    book_text = get_book_text()  
    return book_text   

book_text = main()  
word_count = nums_of_word(book_text) 
char_text = count_char(book_text) 
true_list = sort_list(char_text)    

print("============ BOOKBOT ============")
print("Analyzing book found at books/frankenstein.txt...")
print("----------- Word Count ----------")
print(f"Found {word_count} total words")
print("--------- Character Count -------")
for item in true_list:
    print(f"{item['char']}: {item['num']}")
print("============= END ===============")

main()

