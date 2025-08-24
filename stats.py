def nums_of_word(main):
    words = main.split()
    return len(words)

def count_char(text):
    counts = {}
    for i in text:
        lower_case = i.lower()
        if lower_case in counts: 
            counts[lower_case] += 1
        else:
            counts[lower_case] = 1
    return counts

def sort_list(char_count_dict):
    sort = []
    for char, num in char_count_dict.items():
        if char.isalpha():
            sort.append({"char": char, "num": num})
    sort.sort(reverse=True, key=lambda item: item["num"])
    return sort