path_to_file = "books/frankenstein.txt"

 
with open(path_to_file, 'r') as f:
    content = f.read()
    

def main(content):
    l = content 

def word_counter(content):  
    words_to_count = content.split()
    count = len(words_to_count)
    print(f"Found {count} total words") 

main(content)
word_counter(content)