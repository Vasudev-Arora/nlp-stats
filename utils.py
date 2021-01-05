from collections import Counter
import os

current_dir = os.getcwd()
file_open = open(current_dir, "r")

def word_count(d_file):
    sum_words = 0
    try:
        lines = d_file.readlines()
        if len(lines) > 0:
            for line in lines:
                clean_text = line.strip()
                sum_words += len(clean_text.split(" "))
        return sum_words

    except:
        raise FileNotFoundError

def line_count(d_file):
    try:
        return len(d_file.readlines())

    except:
        raise FileNotFoundError

def most_common_word(d_file):
    letters = ""
    try:
        lines = d_file.readlines()
        for line in lines:
            clean_text = line.strip()
            letters = "".join(clean_text.split())
            letters += letters

        counter = Counter(letters)
        return counter.most_common(1)

    except:
        raise FileNotFoundError

def average_letters(d_file):
    list_words_count = []

    lines = d_file.readlines()
    for line in lines:
        clean_text = line.strip()
        [list_words_count.append(len(x)) for x in clean_text.split(" ")]

    return int(sum(list_words_count) / len(list_words_count))
