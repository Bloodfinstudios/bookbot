# finds the number of words
def get_num_words(text):
    words = text.split()
    return len(words)


def count_char(text):
    alp_char = {}
    text = text.lower()
    for i in text:
        if i in alp_char:
            alp_char[i] += 1
        else:
            alp_char[i] = 1
    return alp_char

def sort_on(item):
    return item["num"]

def sorted_dictionary(char_dict):
 char_list = []
 for ch in char_dict:
        count = char_dict[ch]
        char_list.append({"char": ch, "num": count})
        char_list.sort(reverse=True, key=sort_on)
 return char_list  


