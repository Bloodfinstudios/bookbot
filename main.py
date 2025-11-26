path_to_file = "books/frankenstein.txt"

 
with open(path_to_file, 'r') as f:
    content = f.read()
    


def main(content):
   print(content) 



main(content)