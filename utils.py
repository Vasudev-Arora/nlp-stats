from collections import Counter
import os
from pathlib import Path

file_name = input("Enter the file name (Eg. random.txt): ")
file_path = Path(os.getcwd()) / file_name
file_open = open(file_path, "r")
lines = file_open.readlines()

def clean_text(text):
    text = text.translate ({ord(c): " " for c in "!@#$%^&*()[]{};:,./<>?\|`~-=_+"})
    return text

def word_count(lines):
    sum_words = 0
    try:
        if len(lines) > 0:
            for line in lines:
                cleaned_text = clean_text(line)
                sum_words += len(cleaned_text.split(" "))
        return sum_words

    except:
        raise FileNotFoundError

def line_count(lines):
    try:
        return len(lines)

    except:
        raise FileNotFoundError

def most_common_letter(lines):
    letters = ""
    try:
        for line in lines:
            cleaned_text = clean_text(line)
            letters = "".join(cleaned_text.split())
            letters += letters

        counter = Counter(letters)
        return counter.most_common(1)[0]

    except:
        raise FileNotFoundError

def average_letters(lines):
    list_words_count = []
    for line in lines:
        cleaned_text = clean_text(line)
        [list_words_count.append(len(x)) for x in cleaned_text.split(" ")]

    return round(sum(list_words_count) / len(list_words_count), 1)
    

if __name__ == "__main__":
    print(f"Average number of letters per word:- {average_letters(lines)}")
    print(f"Most common letter:- {most_common_letter(lines)}")
    print(f"Line Count:- {line_count(lines)}")
    print(f"Word Count:- {word_count(lines)}")
