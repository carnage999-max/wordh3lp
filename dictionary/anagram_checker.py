#import the dictionary.py file
from .dictionary import my_dictionary

def check_anagram(word):
    if word not in my_dictionary:
        print(f"{word} is not  a valid word in the dictionary.")
    anagram_list = list()
    for i in my_dictionary.keys():
        if i == word:
            continue
        if sorted(word) == sorted(i):
            anagram_list.append(i)
        else:
            continue
    if anagram_list == list():
        return None
    return anagram_list        