import json

with open('dictionary/dictionary.json') as f:
        my_dictionary = json.load(f)
with open('dictionary/eng_synonyms.json') as s:
        synonym_dict = json.load(s)
def the_dictionary(search):
    return my_dictionary.get(search.lower().strip(), "Word not Found. Please check your word again")

def synonym_dictionary(search):
        return synonym_dict.get(search.lower().strip())
