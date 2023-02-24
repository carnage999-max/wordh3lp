from itertools import permutations

#import the dictionary.py file
from .dictionary import my_dictionary


def all_real_combinations(word):
    all_word_list = list()
    i = len(word)
    while i <= len(word):
        #make sure that single characters (like 'a', 'f', 'j'...)are not included
        if i == 1:
            break
         #get all permutations of the word
        all_word_list += list("".join(p) for p in permutations(word, i))
        i -= 1
     #make the list contain non-repeated values
    all_word_list = set(all_word_list)
    
    #real_world_list contains permutations of the word that are in the dictionary
    real_word_list = list()
    for words in list(all_word_list):
        if words in my_dictionary:
            real_word_list.append(words)
    return real_word_list
def get_points(word):
    scrabble_points = {
        'a':1, 'b':3, 'c':3,'d':2, 'e':1, 'f':4, 'g':2, 'h':4, 'i':1, 
        'j':8, 'k':5, 'l':1, 'm':3, 'n':1, 'o':1, 'p':3, 'q':10, 'r':1, 
        's':1, 't':1, 'u':1, 'v':4, 'w':4, 'x':8, 'y':4, 'z':10 
    }
    scrabble_word_count = 0
    for i in word:
        scrabble_word_count += scrabble_points[i]
    return scrabble_word_count