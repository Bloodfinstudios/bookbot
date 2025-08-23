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

