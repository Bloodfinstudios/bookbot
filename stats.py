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

    